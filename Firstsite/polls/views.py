from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world, welcome to django")

# Create your views here.
