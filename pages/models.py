from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length =255)
    last_name = models.CharField(max_length =255) 
    designation = models.CharField(max_length =255)
    # 'photos/%Y/%m/%d/' - this will upload image with system date in yyyy/mm/dd
    avatar = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    
    # store the team with first name in db instead of db object 
    def __str__(self) -> str:
        return self.first_name