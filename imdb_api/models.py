from django.db import models 
from django.core.validators import MaxValueValidator , MinValueValidator 
from django.contrib.auth.models import User

# Create your models here. 

class StreamPlatform(models.Model): 

    name = models.CharField(max_length=100)
    about = models.CharField(max_length=200) 
    website = models.URLField(max_length=200)  
      
    def __str__(self):
            return self.name



class WatchList(models.Model):  

    title = models.CharField(max_length=100) 
    storyLine = models.CharField(max_length=200) 
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watch_list")   
    avg_rating = models.FloatField(default=0) 
    number_rating = models.IntegerField(default=0)
    active = models.BooleanField(default=True) 
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
         return self.title 
    

class Review(models.Model): 
     
     review_user = models.ForeignKey(User,on_delete=models.CASCADE)
     rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)]) 
     desc = models.CharField(max_length=100)
     watchlist = models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name="reviews")
     active = models.BooleanField(default=True)
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)

     def __str__(self): 
        string = str(self.rating) + " " + str(self.watchlist.title)
        return string
    