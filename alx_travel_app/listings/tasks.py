from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(to_email, booking_details):
    subject = 'Booking Confirmation'
    message = f'Your booking details: {booking_details}'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [to_email])
