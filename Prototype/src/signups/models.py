from django.db import models

# special characters for foreign languages (ex. accents)
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model):
    # basic user information
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    
    # auto_now_add: when created make timestamp
    # auto_now: when updated or changed, make a note of that timestamp
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    # status
    diamond = 'd';
    platinum = 'p';
    gold = 'g';
    silver = 's';
    bronze = 'b';
    
    status_choices = (
        (bronze, 'Bronze'),
        (silver, 'Silver'),
        (gold, 'Gold'),
        (platinum, 'Platinum'),
        (diamond, 'Diamond'),
    )
    
    status = models.CharField(max_length=1,
                              choices=status_choices,
                              default=bronze);
    
    def __unicode__(self):
        return smart_unicode(self.email)