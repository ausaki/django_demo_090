# Create your views here.
from django.utils.httpwrappers import HttpResponse
from .models.polls import Poll
import django.models.polls as polls

def index(request):
    print(polls._MODELS)
    print(dir(polls.polls))
    
    return HttpResponse('hello world')