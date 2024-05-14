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


def meetup_details(request, meetup_slug):
    selected_meetup = {
        'title': 'Second Meetup',
        'location': 'Sibiu',
        'slug': 'second-meetup'
    }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['location']
    })
