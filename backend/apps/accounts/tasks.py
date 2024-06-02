from celery import shared_task
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def remove_not_active_user():
    User.objects.filter(is_active=False).delete()


# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from celery import shared_task
# from apps.accounts.models import User


# @shared_task
# def print_after_3s():
#     # sleep(20)
#     print("hello how are you !")
#     user = User.objects.get(id=1)
#     user.phone = "4444444"
#     user.save()
#

# @shared_task
# def send_mail(
#         subject: str,
#         to: list | str,
#         template: str,
#         context: dict = None,
#         from_email=settings.DEFAULT_FROM_EMAIL,
# ):
#     html_content = render_to_string(template, context=context or {})
#     msg = EmailMultiAlternatives(
#         subject,
#         html_content,  # Fixed the issue: pass HTML content as message content
#         from_email,
#         to if isinstance(to, list) else [to]
#     )
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()

# @shared_task
# def send_mail(
#         subject: str,
#         to: list | str,
#         template: str,
#         context: dict = None,
#         from_email=settings.DEFAULT_FROM_EMAIL,
# ):
#     html_content = render_to_string(template, context=context or {})
#     msg = EmailMultiAlternatives(
#         subject, subject, from_email, to if isinstance(to, list) else [to]
#     )
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()
