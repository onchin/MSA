from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=50, default=None)
    startDate = models.DateTimeField(default=timezone.now, blank=True)
    endDate = models.DateTimeField(default=timezone.now, blank=True)
    active = models.BooleanField(_('active'), default=True)
    lastModifiedBy = models.CharField(max_length=50, default=None)
    lastModifiedDate = models.DateTimeField(default=timezone.now, blank=True)


class League(models.Model):
    leagueName = models.CharField(max_length=50, default=None)
    active = models.BooleanField(_('active'), default=True)
    lastModifiedBy = models.CharField(max_length=50, default=None)
    lastModifiedDate = models.DateTimeField(default=timezone.now, blank=True)


class Location(models.Model):
    locationName = models.CharField(max_length=50, default=None)
    FieldNumber = models.IntegerField(blank=True, null=True)
    indoor = models.BooleanField(_('Y'), default=True)
    locationContactID = models.IntegerField(blank=True, null=True)
    address1 = models.CharField(max_length=50, default=None)
    address2 = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)
    state = models.CharField(max_length=50, default=None)
    zipcode = models.CharField(max_length=50, default=None)
    active = models.BooleanField(_('active'), default=True)
    lastModifiedBy = models.CharField(max_length=50, default=None)
    lastModifiedDate = models.DateTimeField(default=timezone.now, blank=True)


class Team(models.Model):
    teamName = models.CharField(max_length=50, default=None)
    coach = models.IntegerField(blank=True, null=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, default=None, blank=False, null=False)
    active = models.BooleanField(_('active'), default=True)
    lastModifiedBy = models.CharField(max_length=50, default=None)
    lastModifiedDate = models.DateTimeField(default=timezone.now, blank=True)


class Game(models.Model):
    date = models.DateTimeField(default=timezone.now, blank=True)
    startTime = models.DateTimeField(default=timezone.now, blank=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, default=None, blank=False, null=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=None, blank=False, null=False)
    homeTeamID = models.CharField(max_length=50, default=None)
    homeTeamScore = models.IntegerField(blank=True, null=True)
    awayTeamID = models.CharField(max_length=50, default=None)
    awayTeamScore = models.IntegerField(blank=True, null=True)
    tournamentID = models.ForeignKey(Tournament, on_delete=models.CASCADE, default=None, blank=False, null=False)
    active = models.BooleanField(_('active'), default=True)
    lastModifiedBy = models.CharField(max_length=50, default=None)
    lastModifiedDate = models.DateTimeField(default=timezone.now, blank=True)


