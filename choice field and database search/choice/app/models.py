from django.db import models

# Create your models here



# specifying choices

CAR_CHOICES = (
	("1", "Volvo"),
	("2", "Saab"),
	("3", "Opel"),
	("4", "Audi"),
	("5", "hyundai"),
	("6", "suzuki"),
	
)

# declaring a Student Model

class Car(models.Model):
	Car_name = models.CharField(
		max_length = 20,
		choices = CAR_CHOICES,
		default = '1'
		)


class student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    stream=models.CharField(max_length=30)
    
