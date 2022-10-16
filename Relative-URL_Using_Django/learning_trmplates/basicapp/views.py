from django.shortcuts import render

# Create your views here.


def index(request):
    context_dict = {
        'title': "welcome to Index Page"
    }
    return render(request, 'basictemp/index.html', context=context_dict)


def other(request):
    return render(request, 'basictemp/other.html')


def relative(request):
    return render(request, 'basictemp/relative.html')
