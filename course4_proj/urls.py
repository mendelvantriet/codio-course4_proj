"""
URL configuration for course4_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

import gh.views
import movies.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", gh.views.index),

    path("search/", movies.views.search, name="search"),
    path("search-wait/<uuid:result_uuid>/", movies.views.search_wait, name="search_wait"),
    path("search-results/", movies.views.search_results, name="search_results"),
]
