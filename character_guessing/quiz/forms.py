from django import forms
from .models import Question

class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'