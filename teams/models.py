from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_delete, pre_save
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from authentication.models import NewUser
# Create your models here.

class TeamMembers(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    img = models.ImageField(upload_to="image_uploads/userdp/",
                            default='user-default.png')
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, blank=True)
    phone = PhoneNumberField(unique=False, blank=True)
    gender = models.CharField(choices = GENDER_CHOICES,max_length=1,default='M')
    
    def __str__(self):
        return str(self.email)

class Team(models.Model) :
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    leader = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="team", on_delete=models.CASCADE)
    members = models.ManyToManyField(TeamMembers)
    
    def __str__(self):
        return str(self.leader)


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_profile_post_save(sender,instance,created,*args,**kwargs) :
    if created:
        if not TeamMembers.objects.filter(email=instance.email):
            TeamMembers(email=instance.email,name=instance.username,phone=instance.phone, gender='M').save()
            team=Team.objects.create(leader=instance)
            team.members.add(TeamMembers.objects.get(email=instance.email))
            team.save()

        
@receiver(pre_save, sender=settings.AUTH_USER_MODEL)
def create_profile_pre_save(sender, instance,*args, **kwargs):
    if instance is None:
        pass
    else:
        if(TeamMembers.objects.filter(email=instance.email).count()>0):
            team=TeamMembers.objects.get(email=instance.email)
            team.name=instance.username
            team.phone=instance.phone
            team.gender='M'
            team.save()


@receiver(m2m_changed, sender=Team.members.through)
def team_members_changed(sender, instance, *args, **kwargs):
    print(instance)
    user=NewUser.objects.get(email=instance.leader.email)
    user.team_members=instance.members.all().count()
    user.save()

