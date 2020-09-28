from django.shortcuts import render
from . import forms
from .models import JournalModel
from .filters import JournalFilter


def form_name_view(request):
    form = forms.formName()
    if request.method == 'POST':
        form = forms.formName(request.POST)
        if form.is_valid():
            jModel =  JournalModel()
            jModel.title = form.cleaned_data['title']
            jModel.description = form.cleaned_data['description']
            jModel.author = form.cleaned_data['author']
            jModel.save()
            print("Validation Success")

    return render(request, 'basicapp/form_page.html', {'form': form})


def index(request):
    Journal_list = JournalModel.objects.all()
    journal_filter = JournalFilter(request.GET, queryset=Journal_list)
    return render(request, 'basicapp/index.html', {'filter': journal_filter})
