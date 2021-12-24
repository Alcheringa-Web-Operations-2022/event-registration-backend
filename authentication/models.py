import uuid
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


def create_new_ref_number():
    alcherid = "ALC-"
    alcherid += str(NewUser.objects.count()+5001)+"-"
    alcherid += get_random_string(length=4)
    if NewUser.objects.filter(alcherid=alcherid).exists():
        return create_new_ref_number()
    return alcherid

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email,  ** other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    interest_choices = [('dance', 'Dance'), ('music', 'Music'), ('stagecraft', 'Stagecraft'), ('fashion', 'Fashion'), ('classapart', 'Class Apart'), ('arttalkies',
                                                                                                                                                         'Art Talkies'), ('literacy', 'Literacy'), ('digitaldextirity', 'Digital Dextirity'), ('lightscameraaction', 'Lights Camera Action'), ('informals', 'Informals')]
    alcherid = models.CharField(
        max_length=255, blank=True, unique=True)
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    img = models.ImageField(upload_to="image_uploads/userdp/",
                            default='user-default.png')
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    collegename = models.CharField(max_length=150, unique=False)
    city = models.CharField(max_length=150, unique=False)
    fullname = models.CharField(max_length=150, blank=True)
    phone = PhoneNumberField(unique=False, blank=True)
    interest = models.CharField(choices=interest_choices, max_length=127,blank=True,null=True)
    team_members=models.IntegerField(default=0)
    no_of_events_registered=models.IntegerField(default=0)

    date_joined = models.DateTimeField(default=timezone.now)
    provider = models.CharField(max_length=200, unique=False, default="email")
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.email)
    
    def save(self, *args, **kwargs):
        self.alcherid = create_new_ref_number()
        return super(NewUser,self).save(*args,**kwargs)
