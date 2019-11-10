from django.urls import path

from .views import persons, single_person

urlpatterns = [
    path('', persons, name='Person List'),
    path('<int:person_id>', single_person, name='Person demo  List'),
]