from django.shortcuts import render
from .tasks import send_emails
# Create your views here.
def send_campaign_emails(request):
    # call celery
    send_emails.delay()
    return render(request,'campaign.html',{})