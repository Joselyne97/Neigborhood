from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField


urlpatterns=[
    url(r'^$', views.welcome, name="welcome"),
    url(r'^profile$', views.user_profile, name='user-profile'),
    url(r'^edit/profile$', views.edit_profile, name="edit-profile"),
    
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

