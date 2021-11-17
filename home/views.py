from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return to index page """

    return render(request, 'home/index.html')


def google(request):
    """ A view to return to google authentication page """

    return render(request, 'home/googlef6bdd563d9a6019b.html')
