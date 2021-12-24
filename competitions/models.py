from django.db import models
import uuid
from authentication.models import NewUser
class Competition(models.Model):
  competition_choices = [('Dance', 'Dance'), ('Music','Music'), ('Stagecraft','Stagecraft'), ('Fashion','Fashion'),( 'Class Appart','Class Appart'), ('Art Talkies','Art Talkies'), ('Literacy','Literacy'), ('Digital Dextirity','Digital Dextirity'), ('Lights Camera Action','Lights Camera Action'), ('Informals','Informals')] 
  id = models.SlugField(primary_key=True, default=uuid.uuid4)
  module = models.CharField(choices = competition_choices, max_length=127)
  event_name = models.CharField(max_length = 255)
  event_desc = models.CharField(max_length = 255) 
  event_rules = models.FileField(upload_to = "image_uploads/rulebooks/", blank=True, null=True)
  max_members = models.IntegerField(default = 1)
  min_members = models.IntegerField(default = 1)
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
    teamname = models.CharField(max_length=255, blank=False, null=True)
    
    def __str__(self):
        return str(self.teamname)

class PreviousPerformance(models.Model):
    event = models.ForeignKey(
        Competition, related_name="event_name2", on_delete=models.CASCADE)
    team = models.ForeignKey(
        CompTeam, related_name="compteams2", on_delete=models.CASCADE)
    link = models.CharField(max_length=2000,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    



