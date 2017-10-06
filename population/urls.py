# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
from django.conf.urls import url,include
from .views import home

urlpatterns = [
    url(r'^', home,name='population_home'),

]
