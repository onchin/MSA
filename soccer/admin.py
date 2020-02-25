from django.contrib import admin
from .models import Tournament, Team, League, Location, Game
# Register your models here.


class TournamentList(admin.ModelAdmin):
    list_display = ('name', 'startDate', 'endDate', 'active', 'lastModifiedBy', 'lastModifiedDate')
    list_filter = ('name', 'startDate', 'active')
    search_fields = ('name', 'startDate')
    ordering = ['startDate']


class TeamList(admin.ModelAdmin):
    list_display = ('teamName', 'coach', 'league', 'active', 'lastModifiedBy', 'lastModifiedDate')
    list_filter = ('teamName', 'coach', 'league')
    search_fields = ('teamName', 'coach', 'league')
    ordering = ['teamName']


class LeagueList(admin.ModelAdmin):
    list_display = ('leagueName', 'active', 'lastModifiedBy', 'lastModifiedDate')
    list_filter = ['leagueName']
    search_fields = ['leagueName']
    ordering = ['leagueName']


class LocationList(admin.ModelAdmin):
    list_display = ('locationName', 'locationContactID', 'address1', 'address2', 'city', 'state', 'zipcode', 'active',
                    'lastModifiedBy', 'lastModifiedDate')
    list_filter = ('locationName', 'locationContactID', 'address1', 'city', 'state', 'zipcode')
    search_fields = ('locationName', 'locationContactID', 'address1', 'city', 'state', 'zipcode')
    ordering = ['locationName']


class GameList(admin.ModelAdmin):
    list_display = ('date', 'startTime', 'location', 'homeTeamID', 'homeTeamScore', 'awayTeamID',
                    'awayTeamScore', 'tournamentID', 'active', 'lastModifiedBy', 'lastModifiedDate')
    list_filter = ('date', 'startTime', 'location', 'homeTeamID')
    search_fields = ('date', 'startTime', 'location', 'homeTeamID')
    ordering = ['date', 'startTime']


admin.site.register(Tournament, TournamentList)
admin.site.register(Team, TeamList)
admin.site.register(League, LeagueList)
admin.site.register(Location, LocationList)
admin.site.register(Game, GameList)

