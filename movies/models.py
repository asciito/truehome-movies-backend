from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Movie(models.Model):
    class Rating(models.TextChoices):
        G    = 'G', _('General Audiences')
        PG   = 'PG', _('Parental Guidance Suggested')
        PG13 = 'PG-13', _('Parents Strongly Cautioned')
        R    = 'R', _('Restricted')
        NC17 = 'NC-17', _('No One 17 And Under Admitted')
        NR   = 'NR', _('Not Rated')

    name: str     = models.CharField(max_length=255)
    slug: str     = models.CharField(max_length=255, unique=True)
    director: str = models.CharField(max_length=255)
    rated: str    = models.CharField(max_length=5, choices=Rating.choices, default='NR')
    actors: dict  = models.JSONField(null=False, default=list)
    released_date: date = models.DateField(null=False)
    created_at: date = models.DateTimeField(auto_now_add=True)
    updated_at: date = models.DateTimeField(auto_now=True)
