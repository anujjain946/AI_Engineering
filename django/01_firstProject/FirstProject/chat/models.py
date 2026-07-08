from django.db import models

# Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

# class ChatMessage(models.Model):
#     sender = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="sent_messages"
#     )
#     receiver = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="received_messages"
#     )
#     message = models.TextField()
#     message_type = models.CharField(
#         max_length=20,
#         default="text"
#     )
#     attachment = models.FileField(
#         upload_to="chat/",
#         null=True,
#         blank=True
#     )
#     is_read = models.BooleanField(default=False)
#     is_delivered = models.BooleanField(default=False)
#     is_deleted = models.BooleanField(default=False)
#     reply_to = models.ForeignKey(
#         "self",
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)