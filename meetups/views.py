from django.shortcuts import render


#from django.http import HttpResponse


# Create your views here.

def hello(request):
    meetups = [
        {
            'title': 'First Meetup',
            'location': 'Cluj',
            'slug': 'first-meetup'
        },
        {
            'title': 'Second Meetup',
            'location': 'Sibiu',
            'slug': 'second-meetup'
        }
    ]

    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })
