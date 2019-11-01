from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save

class Neighbourhood(models.Model):
   
    name=models.CharField(max_length=50)
    description=HTMLField()
    location=models.CharField(max_length=40)
    police_contact=models.IntegerField(default='112')
    hospital_contact=models.IntegerField(default='911')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def save_hood(self):
        self.save()

    def update_hood(self):
        self.update()

    def delete_rhood(self):
        self.delete()

    
    @classmethod
    def get_hood_by_id(cls,id):
        hood=Neighbourhood.objects.get(id=id)
        return hood


    @classmethod
    def search_by_title(cls,search_term):
        hood=cls.objects.filter(name__icontains=search_term)
        return hood

    def __str__(self):
        return self.name

    

class Profile(models.Model):

    # bio = HTMLField()
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,null=True, default='Kigali')
    # profile_pic = models.ImageField(upload_to = 'pic/', blank=True, null=True)
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    # post_save.connect(save_user_profile, sender=User)

    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

    def __str__(self):
        return self.user

    @classmethod
    def get_user_by_hood(cls, id):
        profile = Profile.objects.filter(hood_id=id).all()
        return profile




class Business(models.Model):
    business_name=models.CharField(max_length=40)
    business_description=HTMLField()
    business_email=models.EmailField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    hood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE, null=True,blank=True)

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()

    def __str__(self):
        return self.business_name

    @classmethod
    def get_business_by_id(cls,id):
        business=Business.objects.get(id=id)
        return business

    @classmethod
    def get_businesses(cls,id):
        businesses=Business.objects.filter(hood_id=id).all()
        return businesses

    # @classmethod
    # def search_by_title(cls,search_term):
    #     business = cls.objects.filter(title__icontains=search_term)
    #     return business


class Joining(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE )
    hood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    def save_joining(self):
        self.save()

    def delete_joining(self):
        self.delete()

    def update_joining(self):
        self.update()


class Post(models.Model):
    topic=models.CharField(max_length=80)
    description=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    hood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)


    def __str__(self):
        return self.topic

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):
        self.update()

    @classmethod
    def get_post_by_hood(cls,id):
        post = Post.objects.filter(hood_id=id).all()
        return post













