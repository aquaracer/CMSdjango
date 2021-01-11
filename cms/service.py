from django.core.mail import send_mail


def send_message(email):
    send_mail(
        subject='test',
        message='Here is the message.',
        from_email=email,
        recipient_list=['test@codestudio.org'],
        fail_silently=False)
