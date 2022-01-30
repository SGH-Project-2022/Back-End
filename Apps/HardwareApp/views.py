from concurrent.futures import thread
from django.db import DatabaseError
from django.shortcuts import render
import os
from django.http import HttpResponse
import socketio
from django.contrib.auth.models import User



async_mode = None

basedir = os.path.dirname(os.path.realpath(__file__))

sio = socketio.Server(async_mode=None , cors_allowed_origins = '*' )

thread = None

#Create your views here.


def index(request):
    global thread
    if thread is None:
        thread = sio.start_background_task(background_thread)
    return render(request, 'index.html')


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        sio.sleep(10)
        count += 1
        sio.emit('my_response', {
            'data': 'Server generated event'}, namespace='/test')


@sio.event
def send(sid, data):
    message = data['message']
    sio.emit('my_response', {
        'message': message,
    })

