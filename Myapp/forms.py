from django import forms
from django.forms import ModelForm, inlineformset_factory

#My imports
from . models import Classroom_Food, Classroom

class Classroom_Food_Form(ModelForm):


    def __init__(self, *args, **kwargs):
        super(Classroom_Food_Form, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    class Meta:

        model = Classroom_Food
        fields = [
            "food",
            "classroom",
            "liked",
            "disliked",
        ]

class ClassroomForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClassroomForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:

        model = Classroom
        fields = [
            'name',
            'school',
        ]
        