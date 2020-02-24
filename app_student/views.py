from django.shortcuts import render, HttpResponse, redirect
from app_login.models import Users, Proposals, Features, Wireframes, Reviews
from .forms import WireframeForm
from django.core.files.storage import FileSystemStorage

# from .forms import Section_1_form
# new:
def student_dashboard(request):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    creator_proposals = Proposals.objects.filter(manager = this_user)
    context = {
        "this_user": this_user,
        "creator_proposals": creator_proposals,
    }
    return render(request, "dash_student1.html",  context)

def log_out(request):
    request.session.clear()
    return redirect ('/')
# new:
def help(request):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    creator_proposals = Proposals.objects.filter(manager = this_user)
    context = {
        "this_user": this_user,
        "creator_proposals": creator_proposals,
    }
    return render(request, "instructions.html",  context)

def projects_page(request):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    creator_proposals = Proposals.objects.filter(manager = this_user)
    context = {
        "this_user": this_user,
        "creator_proposals": creator_proposals,
    }
    return render(request, "projects.html",  context)



def page_all_proposals(request):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    creator_proposals = Proposals.objects.filter(manager = this_user)
    print(creator_proposals)
    joined_proposals = Proposals.objects.filter(student = this_user)
    print("*"*30)
    print(joined_proposals)
    context = {
        "this_user": this_user,
        "creator_proposals": creator_proposals,
        "all_joined_p": joined_proposals,
    }
    return render(request, "all_proposals.html",  context)

def new_create_proposal_page(request):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    creator_proposals = Proposals.objects.filter(manager = this_user)
    # last = creator_proposals[len(creator_proposals)-1]
    all_inst = Users.objects.filter(position = "instructor")

    # FORMS:
    context = {
        "this_user": this_user,
        "creator_proposals": creator_proposals,
        "proposal": creator_proposals,

        # "proposal": last,
        # "all_instructors": all_inst,
        # "form": form,
    }
    return render(request, "new_create_proposal.html", context)

def new_proposal_created(request):
    this_id = request.session['userid']
    creator = Users.objects.get(id = this_id)

    stack_from_f = request.POST['html_stack'] 
    pr_name_from_f= request.POST['html_pr_name']
    aud_from_f = request.POST['html_aud']
    brief_from_f = request.POST['html_brief']
    stack_c_from_f = request.POST['html_stack_comp'] 
    database_from_f= request.POST['html_datab']
    api_from_f = request.POST['html_api']
    server_from_f = request.POST['html_server']
    other_tech_from_f = request.POST['html_other_tech']
    work_distr_from_f = request.POST['html_work_contr']

    new_proposal = Proposals.objects.create(stack = stack_from_f, project_name = pr_name_from_f, audience = aud_from_f, brief = brief_from_f, stack_comp = stack_c_from_f, database = database_from_f, api = api_from_f, server = server_from_f, other_tech = other_tech_from_f, work_contrib = work_distr_from_f, manager = creator) 

    c = int(request.POST['count'])
    for i in range(c):
        print(type('count'+str(i)))
        feat_from_f = request.POST['count'+str(i+1)]
        priority_from_f = request.POST['html_priority']
       # proposal_name_f = request.POST['html_proposal'] 
       # proposal_f = Proposals.objects.get(project_name = proposal_name_f)
        new_feature = Features.objects.create(feat_content = feat_from_f, priority = priority_from_f,  manager = creator)
        new_feature.proposal = new_proposal
        new_feature.save()

    # feat_from_f = request.POST['html_feature']
    # priority_from_f = request.POST['html_priority']
    # new_feature = Features.objects.create(feat_content = feat_from_f, priority = priority_from_f, manager = creator)

    return redirect('/student/create_wireframe_page/'+str(new_proposal.id))









def create_wireframe_page(request, proposal_id):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    # creator_proposals = Proposals.objects.filter(manager = this_user)
    this_proposal = Proposals.objects.get(id = proposal_id)
    form = WireframeForm(request.POST, request.FILES)
    wireframe = Wireframes.objects.all()
    x = Proposals.objects.get(id = proposal_id)
    y = x.wireframes.all()


    context = {
        'form' : form,
        "this_user": this_user,
        "this_proposal": this_proposal,
        'wireframe': wireframe,
        "y": y,

        # "creator_proposals": creator_proposals,
        # "proposal": creator_proposals,
    }
    return render(request, "create_wireframe.html", context)


# FROM MAX:
def create_wireframe(request, proposal_id):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    this_proposal = Proposals.objects.get(id = proposal_id)
    creator_proposals = Proposals.objects.filter(manager = this_user)
    # THis is where upload img logic is
    wireframe = Wireframes.objects.all()
    if request.method == 'POST':
        form = WireframeForm(request.POST, request.FILES)
        print("not broken 1") 
        if form.is_valid() == True:
            form.save()
            print("form is valid")
            return redirect('/student/create_wireframe_page/'+str(proposal_id))
            # return render(request, "create_wireframe.html", {
            # 'form' : form,
            # 'wireframe': wireframe,
            # "this_user": this_user,
            # "this_proposal": this_proposal,

            # })
        else: 
            form = WireframeForm()
            print("something is fucked 1 ")
        return redirect('/student/create_wireframe_page/'+str(proposal_id))

        # return render(request, "create_wireframe.html", {
        #     'form' : form,
        #     'wireframe': wireframe,
        #     "this_user": this_user,
        #     "this_proposal": this_proposal,

        # })
    else: 
        form = WireframeForm()
        print("something is fucked 2 ")
    return redirect('/student/create_wireframe_page/'+str(proposal_id))

    # return render(request, "create_wireframe.html", {
    #     'form' : form,
    #     'wireframe': wireframe,
    #     "this_user": this_user,
    #     "this_proposal": this_proposal,

    # })

def remove_logic(request, id):
    wireframes = Wireframes.objects.all()
    form = WireframeForm(request.POST, request.FILES)
    x = Wireframes.objects.get(id=id)
    x.delete()
    return render(request, "create_wireframe.html", {
        'form' : form,
        'wireframe': wireframes, 
    })






# def create_prop_1(request):
#     user_id_var = request.session['userid']
#     this_user = Users.objects.get(id = user_id_var)
#     creator_proposals = Proposals.objects.filter(manager = this_user)
#     last = creator_proposals[len(creator_proposals)-1]
#     all_inst = Users.objects.filter(position = "instructor")

#     # FORMS:
#     # form = Section_1_form(request.POST)
#     context = {
#         "this_user": this_user,
#         "creator_proposals": creator_proposals,
#         "proposal": last,
#         # "all_instructors": all_inst,
#         # "form": form,
#     }
#     return render(request, "create_pro_0.html", context)

# def create__sect_1(request):
#     #     errors = Trips.objects.trip_validator(request.POST)
#     # if len(errors) > 0:
#     #     for k,v in errors.items():
#     #         messages.error(request, v)
#     #     return redirect ('/trips/new')
#     # else:

#     this_id = request.session['userid']
#     creator = Users.objects.get(id = this_id)

#     stack_from_f = request.POST['html_stack'] 
#     pr_name_from_f= request.POST['html_pr_name']
#     aud_from_f = request.POST['html_aud']
#     brief_from_f = request.POST['html_brief']
#     new_proposal = Proposals.objects.create(stack = stack_from_f, project_name = pr_name_from_f, audience = aud_from_f, brief = brief_from_f, manager = creator) 
#     # add feature to Proposal:
#     return redirect('/student/create_proposal_page')


# def update_lastproposal_s4(request, proposal_id):
#     this_id = request.session['userid']
#     creator = Users.objects.get(id = this_id)
#     this_last_proposal = Proposals.objects.get(id = proposal_id)

#     stack_c_from_f = request.POST['html_stack_comp'] 
#     database_from_f= request.POST['html_datab']
#     api_from_f = request.POST['html_api']
#     server_from_f = request.POST['html_server']
#     other_tech_from_f = request.POST['html_other_tech']
#     this_last_proposal.stack_comp = stack_c_from_f
#     this_last_proposal.save()
#     this_last_proposal.database = database_from_f
#     this_last_proposal.save()
#     this_last_proposal.api = api_from_f
#     this_last_proposal.save()
#     this_last_proposal.server = server_from_f
#     this_last_proposal.save()
#     this_last_proposal.other_tech = other_tech_from_f
#     this_last_proposal.save()
#     return redirect('/student/create_proposal_page')

# def update_lastproposal_s5(request, proposal_id):
#     this_id = request.session['userid']
#     creator = Users.objects.get(id = this_id)
#     this_last_proposal = Proposals.objects.get(id = proposal_id)
#     work_distr_from_f = request.POST['html_work_contr']
#     this_last_proposal.work_contrib = work_distr_from_f
#     this_last_proposal.save()
#     return redirect('/student/create_proposal_page')




def details_proposal(request, proposal_id):
    this_proposal = Proposals.objects.get(id = proposal_id)
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    all_inst = Users.objects.filter(position = "instructor")
    wireframe = Wireframes.objects.all()
    x = Proposals.objects.get(id = proposal_id)
    y = x.wireframes.all()
    context = {
        "this_user": this_user,
        "proposal": this_proposal,
        "all_instructors": all_inst,
        'wireframe': wireframe,
        "y": y,
    }
    return render(request, "proposal_details.html", context)

# FROM SHERY:
# def create_feature(request):
#     this_id = request.session['userid']
#     creator = Users.objects.get(id = this_id)
#     c = int(request.POST['count'])
#     for i in range(c):
#         print(type('count'+str(i)))
#         feat_from_f = request.POST['count'+str(i+1)]
#         priority_from_f = request.POST['html_priority']
#         proposal_name_f = request.POST['html_proposal'] 
#         proposal_f = Proposals.objects.get(project_name = proposal_name_f)
#         Features.objects.create(feat_content = feat_from_f, priority = priority_from_f, proposal = proposal_f, manager = creator)
#     return redirect('/student/create_pro_0_page')

    # OLD one:
    # this_id = request.session['userid']
    # creator = Users.objects.get(id = this_id)

    # feat_from_f = request.POST['html_feature']
    # priority_from_f = request.POST['html_priority']
    # proposal_name_f = request.POST['html_proposal'] 
    # proposal_f = Proposals.objects.get(project_name = proposal_name_f)
    # Features.objects.create(feat_content = feat_from_f, priority = priority_from_f, proposal = proposal_f, manager = creator)
    
    # return redirect('/student/create_proposal_page')

def send_proposal(request, proposal_id):
    this_id = request.session['userid']
    creator = Users.objects.get(id = this_id)
    inst_lname = request.POST['html_inst']
    instructor = Users.objects.get(last_name = inst_lname)
    proposal_to_update = Proposals.objects.get(id = proposal_id)
    proposal_to_update.instructor = instructor
    proposal_to_update.save()
    return redirect('/student/all_proposals')

def delete_proposal(request, proposal_id):
    proposal_to_delete = Proposals.objects.get(id = proposal_id)
    proposal_to_delete.delete()
    return redirect('/student/all_proposals')

def delete_feature(request, feature_id):
    feature_to_delete = Features.objects.get(id = feature_id)
    feature_to_delete.delete()
    return redirect('/student/create_proposal_page')


def all_reviews(request):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    creator_proposals = Proposals.objects.filter(manager = this_user)
    all_reviews = Reviews.objects.all()

    context = {
        "this_user": this_user,
        "creator_proposals": creator_proposals,
        "all_reviews": all_reviews,
    }
    return render(request, "all_reviews.html",  context)

def review_details(request, reviews_id):
    this_review = Reviews.objects.get(id = reviews_id)
    this_instructor = Users.objects.get(review_from_instr = this_review)
    this_proposal = this_review.proposal
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    all_reviews = Reviews.objects.all()
    review_to_update = this_review
    review_to_update.status_rev = "old"
    review_to_update.save()
    context = {
        "this_user": this_user,
        "proposal": this_proposal,
        "all_reviews": all_reviews,
        "this_instructor": this_instructor,
        "this_review": this_review,
    }
    return render(request, "review_details.html", context)

def manage(request):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    creator_proposals = Proposals.objects.filter(manager = this_user)
    print(creator_proposals)
    print("*"*50)
    # print(creator_proposals[0].student)
    print("*"*50)

    all_students = Users.objects.filter(position = "student")
    print(all_students)
    context = {
        "this_user": this_user,
        "creator_proposals": creator_proposals,
        "all_students": all_students,
    }
    return render(request, "manage.html", context)





# FROM SHERRY MANAGE:

def choose_proj(request):
    proposal_f_f = request.POST['html_proposal'] 
    this_proposal = Proposals.objects.get(project_name = proposal_f_f)
    id = this_proposal.id
    print(id)
    return redirect('/student/assignfea/'+str(id))

def assign_feature(request,id):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    this_proposal = Proposals.objects.get(id = id)
    all_students = Users.objects.filter(position = "student")
    
    context = {
        "this_user": this_user,
        "features": this_proposal.features.all(),
        "all_students": all_students,
        "creator_proposals": this_proposal,
    }
    return render(request, "feature.html", context)


def todo(request):
    user_id_var = request.session['userid']
    this_user = Users.objects.get(id = user_id_var)
    manp = Proposals.objects.filter(manager = this_user)
    stp = Proposals.objects.filter(student = this_user)
    
    if len(manp)!= 0 and len(stp) != 0:
        for p in manp:
            print(p)
            if p.status == 'approved':
                man_feature = Features.objects.filter(manager = user_id_var)
                st_feature = Features.objects.filter(student = user_id_var).order_by('priority')
                print("*"*100)
                print(st_feature)
                print("*"*100)
                context = {
                    "map":manp,
                    "stp":stp,
                    "this_user": this_user,
                    "feature": man_feature,
                    "feature1": st_feature,
                }
                print("HELLO 6")

                return render(request, "task.html", context)
    elif len(stp) != 0:
        print("HELLO 1")

        for p in stp:
            print("HELLO 2")

            if p.status == 'approved':
                st_feature = Features.objects.filter(student = user_id_var).order_by('priority')
                print("HELLOOOOOO")
                print(st_feature)
                context = {
                    "this_user": this_user,
                    "feature": st_feature,
                }
                return render(request, "task.html", context)
    elif len(manp)!= 0 :
        for p in manp:
            print(p)
            if p.status == 'approved':
                man_feature = Features.objects.filter(manager = user_id_var)
                context = {
                    "this_user": this_user,
                    "feature": man_feature,

                }

                return render(request, "task.html", context)
    else:
        return redirect('/student')



def compl_feature(request,f_id):
    this_feature = Features.objects.get(id = f_id)
    this_feature.status = 'done'
    this_feature.save()
    print(this_feature.status)
    return redirect('/student/todo')


def assign(request):
    this_id = request.session['userid']
    creator = Users.objects.get(id = this_id)
    newList = request.POST.getlist('checks[]')
    this_student = request.POST.get('html_student')
    s = Users.objects.filter(first_name = this_student)[0]
    id = 0
    for i in newList:
        print(i)
        this_feature = Features.objects.get(id = i)
        con = this_feature.feat_content
        pri = this_feature.priority
        pro = this_feature.proposal
        id = this_feature.proposal.id
        if s.id != this_id:
            new_feature = Features.objects.create(feat_content = con, priority = pri, proposal = pro,student = s)
            this_feature.delete()
            this_feature = Features.objects.get(id = new_feature.id)
            pro.student.add(s)
            s.proposal_joined.add(pro)
    
        this_feature.status = 'assign'
        this_feature.save()

    # new_proposal.features.set([new_feature.id])
    # new_proposal.save()
    return redirect('/student/assignfea/'+str(id))

    # def assign(request):
#     this_id = request.session['userid']
#     creator = Users.objects.get(id = this_id)

#     student_fname = request.POST['html_student']
#     proposal_f_f = request.POST['html_proposal'] 
#     this_proposal = Proposals.objects.get(project_name = proposal_f_f)
#     this_student = Users.objects.get(first_name = student_fname)
#     this_proposal.student.add(this_student)
#     # new_proposal.features.set([new_feature.id])
#     # new_proposal.save()
#     return redirect('/student/manage')


    



