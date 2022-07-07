import os
from datetime import datetime
from multiprocessing import context
from django.conf import settings
from twilio.twiml.messaging_response import MessagingResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

account_sid = "ACca7333bea5f83cec03b623a57780e4b8"
auth_token = "149b2bffe7f1e7bd3e5e4aa1a736afdb"


@csrf_exempt
def message(request):
    submit_message = request.POST.get('userinput')
    rec_time = datetime.now().strftime("%I:%M %p")
    recieve = recieve_message(request)
    # Send_message(submit_message)
    context = {
        'time': rec_time, 'sent_message': submit_message, 'recieve_message': recieve}
    return render(request, 'whatsapp/index.html', context)


def Send_message(message):
    client = Client(account_sid, auth_token)
    send_message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message,
        to='whatsapp:+12679020231'
    )
    print(send_message.sid)


@csrf_exempt
def recieve_message(request):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    print(f'{user} says {message}')
    return message
