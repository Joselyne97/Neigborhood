from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.dispatch import receiver

class Neighbourhood(models.Model):
    places=(
        ('Kicukiro','Kicukiro'),('Remera','Remera'),('Gatenga','Gatenga'),('Gisozi','Gisozi'),('Kacyiru','Kacyiru'),('Karuruma','Karuruma'),('Gatsata','Gatsata'),('Nyamirambo','Nyamirambo'),('Nyamata','Nyamata'),('Huye','Huye'),('Gisenyi','Gisenyi'),('Kibuye','Kibuye')
    )
    name=models.CharField(max_length=200)
    description=HTMLField()
    location=models.CharField(max_length=40, choices=places)
    pub_date = models.DateTimeField(auto_now_add=True)
    police_contact=models.IntegerField(default='112')
    hospital_contact=models.IntegerField(default='911')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def save_neighbourhood(self):
        self.save()

    def update_neighbourhood(self):
        self.update()

    def update_occupants(self):
        self.update()


    def delete_neighbourhood(self):
        self.delete()

    
    @classmethod
    def get_neighbourhoods(cls):
        neighbourhoods=Neighbourhood.objects.objects.all()
        return neighbourhoods

    @classmethod
    def find_neighbourhood_by_id(cls,id):
        neighbourhood=Neighbourhood.objects.get(id=id)
        return neighbourhood

    @classmethod
    def search_by_title(cls,search_term):
        neighbourhood=cls.objects.filter(name__icontains=search_term)
        return neighbourhood

    def __str__(self):
        return self.name

    

class Profile(models.Model):

    bio = HTMLField()
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hood = models.OneToOneField(Neighbourhood, on_delete=models.CASCADE, blank =True,null=True, default='Kigali')

    @classmethod
    def update_profile(cls,id,value):
        cls.objects.filter(id=id).update(user_id = new_user)

    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

    def __str__(self):
        return self.user




