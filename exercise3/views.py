# views.py
from django.http import JsonResponse
from .models import Message

def submit_message(request):
    # Code to save message
    pass

def get_messages(request, receiver):
    messages = Message.objects.filter(receiver=receiver).order_by('-timestamp')[:20]
    data = list(messages.values('sender', 'receiver', 'content', 'timestamp'))
    return JsonResponse(data, safe=False)