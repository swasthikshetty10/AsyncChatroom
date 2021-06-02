from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
# Create your views here.

username = None

def home(request):
    return render(request , 'index.html')
@csrf_exempt
def chat(request):
    content = request.POST
    global username
    username = content['user_name']
    return HttpResponseRedirect(f"/chat/{content['room_name']}")

def room(request , room_name):
    return render(request , 'chatroom.html' , {'room_name' : room_name , "username" : username})
    