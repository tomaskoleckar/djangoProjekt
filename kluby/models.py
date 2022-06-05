from django.db import models
from django.urls import reverse


class Competition(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Competition name',
    help_text='Enter a club competition (e.g. Champions league, LaLiga)')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Klub(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    nation = models.CharField(blank=True, null=True,max_length=200, verbose_name='Nation')
    info = models.TextField(blank=True, null=True, verbose_name='Info')
    established = models.DateField(blank=True, null=True,
                                    help_text='Please use the following format: <em>YYYYMM-DD</em>.',
                                    verbose_name='Established')
    domestic_champions = models.IntegerField(blank=True, null=True,
                                  help_text='Please enter an integer value',
                                  verbose_name='League titles')
    poster = models.ImageField(upload_to='klub/logo/%Y/%m/%d/', blank=True, null=True,
                               verbose_name="Logo")
    europe_rating = models.IntegerField(blank=True, null=True,
                                             help_text='Please enter an integer value',
                                             verbose_name='Europe rank')
    competitions = models.ManyToManyField(Competition, help_text='Select a competitions for this club')

    class Meta:
        ordering = ['europe_rating', 'name']

    def __str__(self):
        return f'{self.name}, year: {str(self.established.year)}, europe_rating:{str(self.europe_rating)}'

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])