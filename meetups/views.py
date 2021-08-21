from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello World")

# address will start at templates folder
def index(request):
    meetups = [
        {
            "title": "A first meetup", 
            'location': 'New York', 
            'slug':'a-first-meetup'
        }, 
        {
            "title": "A second meetup", 
            'location': 'Paris', 
            'slug': 'a-second-meetup'
        }
    ]
    return render(request, "meetups/index.html", {
        "show_meetups": True, 
        "meetups": meetups
    })

# this is just another way to add
def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first meetup'
    }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })