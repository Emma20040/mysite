from django.urls import path
from . import views
#from . import forms

urlpatterns = [
    path('question/', views.question, name='question'),
    path('choice/', views.choice, name='choice' ),
    
    

]

