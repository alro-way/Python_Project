from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from app_login.models import Users, Proposals, Features, Wireframes, Reviews
import bcrypt


def login_page(request):
    # if 'userid' not in request.session:
    #     request.session['userid'] = None
    #     request.session['user_position'] = None
    return render(request, "login.html")

def create_user(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for k,v in errors.items():
            messages.error(request, v)
        return redirect ('/')
    else:
        position_from_form = request.POST['html_position'] 
        fname_from_form = request.POST['html_reg_fname'] 
        lname_from_form = request.POST['html_reg_lname']
        email_from_form = request.POST['html_reg_email']
        # create the hash:  
        password_from_form = request.POST['html_reg_password']
        pw_hash = bcrypt.hashpw(password_from_form.encode(), bcrypt.gensalt()).decode()     
        print(pw_hash)

        new_user = Users.objects.create(position = position_from_form, first_name = fname_from_form, last_name = lname_from_form, email = email_from_form, password = pw_hash)
        request.session['userid'] = new_user.id
        request.session['user_position'] = new_user.position
        messages.success(request, "User successfully created")
        return redirect('/student') 

def login_user(request):
    login_errors = Users.objects.login_validator(request.POST)
    if len(login_errors) > 0:
        for k,v in login_errors.items():
            print(v)
            messages.error(request, v)
        return redirect ('/')
    else:
        user = Users.objects.filter(email = request.POST['html_log_email'])
        if user: 
            logged_user = user[0] 
            if bcrypt.checkpw(request.POST['html_log_pw'].encode(), logged_user.password.encode()):
                print("password match")
                request.session['userid'] = logged_user.id
                request.session['user_position'] = logged_user.position
                print("THIS IS PASSWORD CHECK")
                if logged_user.position == "student":
                    print("THIS IS STUDENT")
                    return redirect('/student')   
                if logged_user.position == "instructor":
                    print("THIS IS INSTRUCTOR")
                    return redirect('/instructor/all_proposals')  
                # here rout of second app html
