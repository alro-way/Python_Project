from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date
import re
import bcrypt


class UsersManager(models.Manager):
    # registration errors:
    def basic_validator(self, postData):
        errors = {}
        if len(postData['html_reg_fname']) < 3:
            errors['html_reg_fname'] = "First name should be at least 2 characters"
        if len(postData['html_reg_lname']) < 3:
            errors["html_reg_lname"] = "Last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['html_reg_email']):              
            errors['html_reg_email'] = "Invalid email address!"
        if len(postData['html_reg_password']) < 8:
            errors["html_reg_password"] = "Password should be at least 8 characters"
        if postData["html_reg_passw_conf"] != postData['html_reg_password']:
            errors["html_reg_password"] = "Passwords do not match"
        if Users.objects.filter(email = postData['html_reg_email']).exists():
            errors['html_reg_email'] = "An User with such email already exists."
        return errors
    # login errors:
    def login_validator(self, postData):
        login_errors = {}
        if not Users.objects.filter(email = postData['html_log_email']).exists():
            login_errors['html_log_email'] = "An User with such email does not exist."

        if Users.objects.filter(email = postData['html_log_email']).exists():
            this_user = Users.objects.get(email = postData['html_log_email'])
            if not bcrypt.checkpw(postData['html_log_pw'].encode(), this_user.password.encode()):
                login_errors['html_log_pw'] = "Login Password does not match."
        return login_errors

class Users(models.Model):
    position = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True, default=None)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()
    
    
class Proposals(models.Model):
    stack = models.CharField(max_length = 50)
    project_name = models.CharField(max_length = 255)
    audience = models.CharField(max_length = 255)
    brief = models.CharField(max_length = 255)
    stack_comp = models.CharField(max_length = 255, blank=True, null=True)
    database = models.CharField(max_length = 255, blank=True, null=True)
    api = models.CharField(max_length = 255, blank=True, null=True)
    server = models.CharField(max_length = 255, blank=True, null=True)
    other_tech = models.TextField(blank=True, null=True)
    work_contrib = models.TextField(blank=True, null=True)
    # status can be: new, approved, not approved
    status = models.CharField(max_length = 50, default="new")
    # relationships instructor relationship is deleted:
    manager = models.ForeignKey(Users, related_name="proposal_created", on_delete=models.CASCADE,null=True, blank=True)
    student = models.ManyToManyField(Users, related_name="proposal_joined")
    instructor = models.ForeignKey(Users, related_name="proposal_instructor", on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(default = datetime.now())
    updated_at = models.DateTimeField(auto_now = True)


class Wireframes(models.Model):
    wireframe_img = models.FileField(upload_to="wireframes/img/")
    # relationships:
    proposal = models.ForeignKey(Proposals, related_name="wireframes", on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(default = datetime.now())
    updated_at = models.DateTimeField(auto_now = True)


class Features(models.Model):
    feat_content = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length = 10, blank=True, null=True)
    status = models.CharField(max_length = 50, default="Not done")

    # relationships:
    proposal = models.ForeignKey(Proposals, related_name="features", on_delete=models.CASCADE,null=True, blank=True)
    student = models.ForeignKey(Users, related_name="feature_joined", on_delete=models.CASCADE,null=True, blank=True)
    manager = models.ForeignKey(Users, related_name="feature_created", on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(default = datetime.now())
    updated_at = models.DateTimeField(auto_now = True)


class Reviews(models.Model):
    review_content = models.TextField(blank=True, null=True)
    status_rev = models.CharField(max_length = 50, default="new")
    # is it many to many or one to one?
    proposal = models.ForeignKey(Proposals, related_name="reviews", on_delete=models.CASCADE,null=True, blank=True)
    instructor = models.ForeignKey(Users, related_name="review_from_instr", on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(default = datetime.now())
    updated_at = models.DateTimeField(auto_now = True)


class Tasks(models.Model):
    task_content = models.TextField(blank=True, null=True)
    student = models.ForeignKey(Users, related_name="student_tasks", on_delete=models.CASCADE,null=True, blank=True)
    feature = models.ForeignKey(Features, related_name="tasks", on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(default = datetime.now())
    updated_at = models.DateTimeField(auto_now = True)

