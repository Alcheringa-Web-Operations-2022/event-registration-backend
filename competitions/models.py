from django.db import models
import uuid
from django.db.models.base import Model
from authentication.models import NewUser
from competitions.validators import validate_file_extension


class Module(models.Model):
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    module = models.CharField(max_length=127)
    module_query_name_without_spaces_all_small = models.CharField(max_length=127)
    module_icon = models.ImageField(
        upload_to="image_uploads/moduleicons/", default='module_icon_default.png')
    def __str__(self):
          return str(self.module)

class Competition(models.Model):
  id = models.SlugField(primary_key=True, default=uuid.uuid4)
  module=models.ForeignKey(Module,related_name='modulename',on_delete=models.CASCADE)
  event_name = models.CharField(max_length = 255)
  event_desc = models.CharField(max_length = 255) 
  event_rules=models.TextField()
  event_rules_pdf = models.FileField(upload_to="image_uploads/rulebooks/", validators=[validate_file_extension],  blank=True, null=True)
  min_members = models.IntegerField(default=1)
  max_members = models.IntegerField(default = 1)
  location = models.CharField(max_length = 63)
  prize_worth = models.IntegerField()
  image = models.ImageField(upload_to="image_uploads/event_pics/", default='event_default.png')
  
  def __str__(self):
      return str(self.event_name)



class CompTeam(models.Model):
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    event = models.ForeignKey(
        Competition, related_name="event_name1", on_delete=models.CASCADE)
    leader = models.ForeignKey(
        NewUser, related_name="teams_leader", on_delete=models.CASCADE)
    members = models.ManyToManyField(
        "teams.TeamMembers", related_name="compteams")
    
    def __str__(self):
        return str(self.leader)

class PreviousPerformance(models.Model):
    event = models.ForeignKey(
        Competition, related_name="event_name2", on_delete=models.CASCADE)
    team = models.ForeignKey(
        CompTeam, related_name="compteams2", on_delete=models.CASCADE)
    link = models.CharField(max_length=2000,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    



