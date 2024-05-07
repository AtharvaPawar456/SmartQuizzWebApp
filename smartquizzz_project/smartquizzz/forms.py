# quizapp/forms.py
from django import forms
from .models import SmartQuizQuestion

class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = SmartQuizQuestion
        fields = '__all__'
