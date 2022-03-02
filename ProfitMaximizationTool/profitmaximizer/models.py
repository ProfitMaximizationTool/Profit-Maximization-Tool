from django.db import models
from django.contrib.auth.models import User

class BusinessOwner(User):
	business_name = models.CharField(max_length=100)
	full_name = models.CharField(max_length=30, blank=True)

	def __str__(self):
		return self.username