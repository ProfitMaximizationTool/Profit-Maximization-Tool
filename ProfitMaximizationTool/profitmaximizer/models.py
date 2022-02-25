from django.db import models
from django.contrib.auth.models import User

class BusinessOwner(User):
	business_name = models.CharField(max_length=100)

	def __str__(self):
		return self.username