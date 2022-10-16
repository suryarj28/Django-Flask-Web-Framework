from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.


def index(request):
    return render(request, 'basictemp/index.html')


def basic_from(request):
    form = forms.Form_name()
    forms_dict = {'forms': form}
    if request.method == 'POST':
        form = forms.Form_name(request.POST)

        if form.is_valid():
            name_data = form.cleaned_data['name']
            email_data = form.cleaned_data['email']
            print(f"Name : {name_data}")
            print(f"Email : {email_data}")

    return render(request, 'basictemp/basicform.html', context=forms_dict)
