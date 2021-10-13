
from django.db import models
from django.db.models.base import Model
'''
class dreamreal(models.Model):

   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()
   online = models.ForeignKey('Online', default = 1,null=True,on_delete=models.SET_NULL)

   class Meta:
      db_table = "dreamreal"
'''
class Comic(models.Model):
   name = models.CharField(max_length = 50)
   genre =  models.CharField(max_length = 50)
   creator = models.ForeignKey('User', default = 1,null = True,on_delete=models.SET_NULL)
   def __str__(self):
        return self.name
   class Meta:
      db_table = "comic"

class User(models.Model):
    username = models.CharField(max_length = 30,null=False,unique=True)
    password = models.CharField(max_length=30,null=False)
    
    class Meta:
      db_table = "user"

class Chapter(models.Model):
    name = models.CharField(max_length = 30)
    comic_id = models.ForeignKey('Comic',default = 1,null = True,on_delete=models.SET_NULL)
    
    class Meta:
      db_table = "chapter"

class Review(models.Model):
      name = models.CharField(max_length = 30)
      comic_id = models.ForeignKey('Comic',default = 1,null = True,on_delete=models.SET_NULL)
      user_id = models.ForeignKey('User',default = 1,null = True,on_delete=models.SET_NULL)
    
      class Meta:
         db_table = "Review"

class Subscription(models.Model):
      comic_id = models.ForeignKey('Comic',default = 1,null = True,on_delete=models.SET_NULL)
      user_id = models.ForeignKey('User',default = 1,null = True,on_delete=models.SET_NULL)
      date = models.DateField()

      class Meta:
         db_table = "subscribtion"