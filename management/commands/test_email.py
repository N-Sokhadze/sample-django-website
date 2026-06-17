from django.core.mail import send_mail 
from django.conf import settings

send_mail(
    'Brevo SMTP QA Test',
    "this confirms brevo SMTP works",
    settings.DEFAULT_FROM_EMAIL,
    [settings.DEFAULT_FROM_EMAIL],
    fail_silently=False,
)