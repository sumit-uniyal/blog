from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_email(subject, to_email, body, cc=None):
    subject = subject
    from_email = settings.EMAIL_HOST_USER
    to_email = to_email
    html_content = body
    
    msg = EmailMultiAlternatives(subject, '', from_email, to_email)
    msg.attach_alternative(html_content, "text/html")

    if not cc:
        cc=[]
    else:
        msg.cc = cc

    msg.send()