"""newsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from newsapp import views
  
urlpatterns = [
    path('', views.index, name ='index'),
    path('admin/', admin.site.urls),
    path('usa', views.usa, name ='usa'),
    path('india', views.india, name ='india'),
    path('business', views.business, name ='business'),
    path('entertainment', views.entertainment, name ='entertainment'),
    path('general', views.general, name ='genral'),
    path('health', views.health, name ='health'),
    path('science', views.science, name ='science'),
    path('sports', views.sports, name ='sports'),
    path('technology', views.technology, name ='technology'),
    # path('us_search', views.search_usa, name ='search'),
    # path('in_search', views.search_india, name ='india'),
    path('<str:name>/search', views.search, name ='search'),
    path('search', views.search_index, name ='search_index'),
]