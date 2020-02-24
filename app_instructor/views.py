from django.shortcuts import render, HttpResponse, redirect
from app_login.models import Users, Proposals, Features, Wireframes, Reviews

def instructor_dashboard(request):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    context = {
        "this_user": this_user,
    }
    return render(request, "instructor_dash.html", context)
    # ask teacher how to use one html from one app

def all_proposals(request):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    proposals = Proposals.objects.filter(instructor = this_user)
    print(proposals)
    context = {
        "this_user": this_user,
        "proposals": proposals,
    }
    return render(request, "inst_proposals.html", context)

def details_prop(request, p_id):
    this_proposal = Proposals.objects.get(id = p_id)
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    wireframe = Wireframes.objects.all()
    x = Proposals.objects.get(id = p_id)
    y = x.wireframes.all()
    context = {
        "this_user": this_user,
        "proposal": this_proposal,
        'wireframe': wireframe,
        "y": y,
    }

    return render(request, "details_prop.html", context)

def save_review(request, proposal_id):
    this_proposal = Proposals.objects.get(id = proposal_id)
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    review_from_f = request.POST['html_brief']
    new_review = Reviews.objects.create(review_content = review_from_f, proposal = this_proposal, instructor = this_user)
    this_review = new_review.review_content
    context = {
        "this_user": this_user,
        "proposal": this_proposal,
        "this_review": this_review,
    }
    return render(request, "details_prop_saved_reviews.html", context)



def prop_approved(request, proposal_id):
    print("IT WORKS")
    this_proposal = Proposals.objects.get(id = proposal_id)
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    proposal_to_update = Proposals.objects.get(id = proposal_id)
    print(proposal_to_update.status)
    proposal_to_update.status = "approved"
    proposal_to_update.save()
    print(proposal_to_update.status)
    return redirect ('/instructor/all_proposals')

def prop_not_approved(request, proposal_id):
    print("IT WORKS")
    this_proposal = Proposals.objects.get(id = proposal_id)
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    proposal_to_update = Proposals.objects.get(id = proposal_id)
    print(proposal_to_update.status)
    proposal_to_update.status = "not_approved"
    proposal_to_update.save()
    print(proposal_to_update.status)
    return redirect ('/instructor/all_proposals')


def reviews_page(request):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    reviews_of_instr = Reviews.objects.filter(instructor = this_user)
    # all_reviews = reviews_of_instr.filter(status = "old")
    all_proposals = Proposals.objects.filter(instructor = this_user)
    context = {
        "this_user": this_user,
        "creator_proposals": reviews_of_instr,
        "all_reviews": reviews_of_instr,
        "all_proposals": all_proposals,
    }
    return render(request, "all_instr_reviews.html",  context)


def details_reviews(request, reviews_id):
    this_review = Reviews.objects.get(id = reviews_id)
    this_proposal = this_review.proposal
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    all_reviews = Reviews.objects.all()
    context = {
        "this_user": this_user,
        "proposal": this_proposal,
        "all_reviews": all_reviews,
        "this_review": this_review,
    }
    return render(request, "review_details_ins.html", context)





def log_out(request):
    request.session.clear()
    return redirect ('/')
