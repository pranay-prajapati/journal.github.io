import django_filters
from .models import JournalModel

class JournalFilter(django_filters.FilterSet):

    class MyMeta:
        model = JournalModel()

        fields = ('title','description','author',)