from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Suggested code may be subject to a license. Learn more: ~LicenseLog:1451482758.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:4221772649.
class Chaivarity(models.Model):
    Select_Chai_Type = [
        ('ML', 'Masala Tea'),
        ('GN', 'Ginger Tea'),
        ('LM', 'Leamon Tea'),
        ('RT', 'Raw Tea'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    cha_type = models.CharField(max_length=2, choices=Select_Chai_Type)
    DisplayField = ['name', 'description', 'chai_type'] 

    def __str__(self):
        return f"{self.name} ({self.cha_type})"



# One to many relationship

class ChaiReview (models.Model):
    chai = models.ForeignKey(Chaivarity, on_delete=models.CASCADE, related_name='Review') # Foreign key from Chaivarity model
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key from User model
    rating = models.IntegerField()
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

# many to many relation

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varity = models.ManyToManyField(Chaivarity, related_name='Stores') # Many to many relationship with Chaivarity model

    def __str__(self):
        return self.name




# Suggested code may be subject to a license. Learn more: ~LicenseLog:2840045714.
class Certificate(models.Model):
   chai = models.OneToOneField(Chaivarity, on_delete=models.CASCADE, related_name='Certificate') # One to one relationship with Chaivarity model
   certificate_number = models.CharField(max_length=50) # Certificate number
   issue_date = models.DateTimeField(default=timezone.now) # Issue date
   expiration_date = models.DateTimeField() # Expiration date
   
   def __str__(self):
        return f'{self.chai.name} certificate' # Display the certificate for the chai