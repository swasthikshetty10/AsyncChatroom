from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'index.html' , {})

def room(request , room_name):
    return render(request , 'chatroom.html' , {'room_name' : room_name})