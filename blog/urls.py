
from django.urls import path, include
from . import views

app_name = 'blog'    #name of the app is blog

urlpatterns = [
    path('', views.allBlogs, name='all_blogs'),
    # path('sports/', views.allSports, name='sports'),
    path('<int:blog_id>/', views.details, name='detail'),

]