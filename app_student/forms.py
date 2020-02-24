from django import forms 
from app_login.models import Wireframes 

class WireframeForm(forms.ModelForm):
    class Meta: 
        model= Wireframes
        fields = ('wireframe_img', 'proposal',)