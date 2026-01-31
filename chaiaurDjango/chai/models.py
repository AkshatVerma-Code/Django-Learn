from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI'),
    ]
    Name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/') 
    date_added = models.DateTimeField(default = timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.Name
    
# One to many
class chaireview(models.Model):
    RATING_CHOICE = [
        ('1 Star',1),
        ('2 Star',2),
        ('3 Star',3),
        ('4 Star',4),
        ('5 Star',5),
    ]
    chai = models.ForeignKey(ChaiVariety,on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.CharField(choices=RATING_CHOICE)
    comment  = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} reviwed {self.chai.Name}"

# many to many
class store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(ChaiVariety,related_name='stores')

    def __str__(self):
        return self.name
    
# one to one

class chaicertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety,on_delete=models.CASCADE,related_name='certificate')    
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()    

    def __str__(self):
        return f'certificate for {self.chai.Name}'