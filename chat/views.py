from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
# Create your views here.



def home(request):
    if request.session.get('user_name', None):
        return render(request , 'index.html',  {'room_name' : "" , "user_name" : request.session['user_name']})
    if request.session.get('room_name', None):
        return render(request , 'index.html',  {'room_name' : request.session['room_name'] , "user_name" : "" })
    
    return render(request , 'index.html' , {'room_name' : "" , 'user_name' : ""})   
@csrf_exempt
def chat(request):
    content = request.POST
    request.session['user_name'] = content['user_name']    
    return HttpResponseRedirect(f"/chat/{content['room_name']}")

def room(request , room_name):
    request.session['room_name'] = room_name
    if not request.session.get('user_name', None) :
        return HttpResponseRedirect("/" , {'room_name' : room_name})
    return render(request , 'chatroom.html' , {'room_name' : room_name , "username" : request.session['user_name']})
    
def changename(request):
    content = request.POST
