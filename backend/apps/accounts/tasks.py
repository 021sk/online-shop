# from celery import shared_task
#
#
# @shared_task
# def print_after_3s():
#     # sleep(20)
#     print("hello how are you !")


# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from celery import shared_task

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
#         subject, subject, from_email, to if isinstance(to, list) else [to]
#     )
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()
