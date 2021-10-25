from django import forms
from .models import Material, Search

class AddMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['course_code', 'title', 'file', 'contributor', 'description',]


