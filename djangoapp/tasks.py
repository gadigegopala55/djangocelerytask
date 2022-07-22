from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

@shared_task(bind=True)
def sending_mail(self,name):
    send_mail(
        "Traveller Blog Subscription","You are Successfully subscribed to Gopala Krishna Blog","demomail224@gmail.com",
        [name]
    )
    return "Done"

@shared_task(bind=True)
def sending_notification(self,name):
    send_mail(
        "Traveller Blog Notification","Gopala Krishna Added New Post in Travellers Blog","demomail224@gmail.com",
        [name]
    )
    return "Done"

