from .views import *
from django.urls import path

urlpatterns=[
    path('',item),
    path('food/<int:id>/',item_id)
]