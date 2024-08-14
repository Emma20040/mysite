from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
from .models import Choice
from .forms import My_form
def question(request):
  if request.method == "POST":
    question_text=request.POST['question']
    pub_date = request.POST['date']
    question = Question(question_text=question_text, pub_date=pub_date)
    question.save()

    return HttpResponse("success")
  return render(request, 'polls/Question.html')
   
def choice(request):
    form=My_form()
    if request.method=="POST":
       form= My_form(request.POST)
       if form.is_valid():
          form.save()
          return HttpResponse('success')
       
    context= {'form':form}
    return render(request, 'polls/Choice.html', context)




# Create your views here.
