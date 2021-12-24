from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_delete, pre_save
from authentication.models import NewUser
from django.db import models
from authentication.models import NewUser
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
import uuid
# Create your models here.

class TeamMembers(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, blank=True)
    phone = PhoneNumberField(unique=False, blank=True)
    gender = models.CharField(choices = GENDER_CHOICES,max_length=1,default='M')
    
    def __str__(self):
        return str(self.email)

class Team(models.Model) :
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    leader = models.OneToOneField(NewUser,related_name="team",on_delete=models.CASCADE)
    members = models.ManyToManyField(TeamMembers)
    
    def __str__(self):
        return str(self.leader)


@receiver(post_save,sender=NewUser)
def create_profile(sender,instance,created,*args,**kwargs) :
    if created:
        Team(leader=instance).save()

        

