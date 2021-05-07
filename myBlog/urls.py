from  django.urls import  path
from . import views

app_name = 'myBlog'
urlpatterns = [
    path('', views.postPage,name='postPage')
    ]