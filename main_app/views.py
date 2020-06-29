from django.shortcuts import render
# from .models import Quiz
from main_app.form import PostForm
# from django.views.generic import CreateView


# Create your views here.
def home(request):
    return render(request, 'base.html')


# class New_search(CreateView):
#     model = Quiz
#     form_class = PostForm
#     template_name = 'new_search.html'
#
#
# def quiz(request):
#     context = {
#         'quizes': Quiz.objects.filter()
#     }
#
#     return render(request, 'new_search.html', context)
def index(request):
  submitbutton= request.POST.get("submit")

  title=''
  start_quiz=''
  end_quiz=''
  description = ''

  form = PostForm(request.POST or None)
  if form.is_valid():
        title= form.cleaned_data.get("title")
        start_quiz= form.cleaned_data.get("start_quiz")
        end_quiz= form.cleaned_data.get("end_quiz")
        description = form.cleaned_data.get("description")
  context= {'form': form, 'title': title,
            'start_quiz': start_quiz, 'submitbutton': submitbutton,
            'end_quiz': end_quiz, 'description': description}

  return render(request, 'new_search.html', context)
