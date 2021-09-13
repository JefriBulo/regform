from django.db import models

# Create your models here.
class User(models.Model):
	id = models.AutoField(primary_key=True)
	mobile_number = models.CharField(max_length=12)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=30)
	month_birth = models.CharField(max_length=15)
	date_birth = models.CharField(max_length=2)
	year_birth = models.CharField(max_length=4)
	gender = models.CharField(max_length=6)
	email = models.CharField(max_length=25)
	date_registered = models.DateField(max_length=15)
	class Meta:
		db_table = "user"
		def __str__(self):
			return self.mobile_number, self.first_name
		
		