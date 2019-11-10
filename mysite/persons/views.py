from django.shortcuts import render
from .models import Person


class PersonController:
    _skip = 0
    _limit = 0
    _filter = {}
    _orderby = 'pk'

    def skips(self, items):
        self._skip = items
        return self

    def limit(self, items):
        self._limit = items
        return self

    def order_by(self, args):
        self._orderby = args
        return self

    def filter(self, **kwargs):
        self._filter = kwargs
        return self

    def get(self):
        persons = Person.objects.all()
        _persons = persons.filter(**self._filter)
        _persons = _persons.order_by(self._orderby)
        if self._limit == 0:
            return _persons[self._skip:]
        return _persons[self._skip: self._skip + self._limit]


def persons(request):
    person_ctrl = PersonController()
    persons = person_ctrl.order_by('-name').get()
    context = {'persons': persons}
    return render(request, 'person_list.html', context)


def single_person(request, person_id):
    persons = Person.objects.filter(id=person_id).all()
    context = {'persons': persons}
    return render(request, 'person_details.html', context)
