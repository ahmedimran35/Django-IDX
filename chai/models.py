from django.db import models
from django.utils import timezone

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

class Meta:
    db_tables = 'Chaivarity'



