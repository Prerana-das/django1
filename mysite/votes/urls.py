from django.urls import path

from .views import votes_index,votes_next

urlpatterns=[
    path('',votes_index,name="votes_index"),
    path('next/', votes_next, name="votes_next")
]