from django.db import models


class Person(models.Model):
    ID = models.CharField(max_length=9, primary_key=True)
    birth_year = models.IntegerField(null=True)
    birth_month = models.IntegerField(null=True)
    birth_day = models.IntegerField(null=True)
    birth_country = models.CharField(max_length=255,null=True)
    birth_state = models.CharField(max_length=255,null=True)
    birth_city = models.CharField(max_length=255,null=True)
    death_year = models.IntegerField(null=True)
    death_month = models.IntegerField(null=True)
    death_day = models.IntegerField(null=True)
    death_country = models.CharField(max_length=255,null=True)
    death_state = models.CharField(max_length=255,null=True)
    death_city = models.CharField(max_length=255,null=True)
    name_first = models.CharField(max_length=255,null=True) 
    name_last = models.CharField(max_length=255,null=True)
    name_given = models.CharField(max_length=255,null=True)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    bats = models.CharField(max_length=255,null=True)
    throws = models.CharField(max_length=255,null=True)
    debut = models.CharField(max_length=255,null=True)
    final_game = models.CharField(max_length=255,null=True)
    retro_id = models.CharField(max_length=255,null=True)
    bbref_id = models.CharField(max_length=255,null=True)
    birth_date = models.DateField(auto_now=False,auto_now_add=False)
    debut_date = models.DateField(auto_now=False,auto_now_add=False)
    final_game_date = models.DateField(auto_now=False,auto_now_add=False)
    death_date = models.DateField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.name_first + ' ' + self.name_last
	