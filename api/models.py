from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication.models import Token


class Employee(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	joining_date=models.DateField()
	emp_id=models.IntegerField()

# This Signal creates Auth Token for Users

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
	if created:
		Token.objects.create(user=instance)
