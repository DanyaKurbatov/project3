from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    start_quiz = forms.DateTimeField()
    end_quiz = forms.DateTimeField()
    description = forms.CharField(max_length=200)
