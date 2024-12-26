from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Event, Category, EventRegistration


# Create your views here.
def index(request):
    categories = Category.objects.all()
    for cat in categories:
        count = len(Event.objects.filter(category_id=cat.id))
        cat.count = count

    return render(request, 'index.html', {'categories' : categories})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if(User.objects.filter(email=email).exists()):
                messages.info(request, 'Email already registered')
                return redirect('signup')
            elif(User.objects.filter(username=username).exists()):
                messages.info(request, 'Username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(email=email, username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password did not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def category(request, cat):
    user = request.user
    categories = Category.objects.all()
    locations = Event.objects.filter(category_id=cat).values_list('city', flat=True).distinct()

    location_filter = request.GET.get('location', '')
    if location_filter:
        events = Event.objects.filter(category_id=cat, city=location_filter)
    else:
        events = Event.objects.filter(category_id=cat)

    events = list(set(events))

    for event in events:
        if user.is_authenticated:
            event.is_registered = EventRegistration.objects.filter(userid=user, eventid=event.id).exists()
        else:
            event.is_registered = False
    count = len(events)

    context = {
        'events': events, 
        'categories': categories, 
        'selected_cat': cat, 
        'location_filter':location_filter, 
        'locations': locations,
        'count': count
    }
    return render(request, 'category.html', context)



def myevents(request, userid):
    location_filter = request.GET.get('location', '')
    user = User.objects.get(id=userid)
    events_list = EventRegistration.objects.filter(userid=user).values_list('eventid', flat=True)
    events = []
    locset = set()
    for i in range(len(events_list)):
        event_details = Event.objects.get(id=events_list[i])
        locset.add(event_details.city)
    locations=list(locset)



    for eventid in events_list:
        if location_filter:
            try:
                event_details = Event.objects.get(id=eventid, city=location_filter)
            except Event.DoesNotExist:
                pass
        else:
            try:
                event_details = Event.objects.get(id=eventid)
            except Event.DoesNotExist:
                pass
        # event_details = Event.objects.get(id=eventid)
        events.append(event_details)
    
    events = list(set(events))
    username = User.objects.get(id=userid)
    count = len(events)

    context = {
        'events': events, 
        'username':username, 
        'locations':locations, 
        'location_filter':location_filter,
        'count': count
    }
    return render(request, 'myevents.html', context)


def registerEvent(request):
    current_url = request.META.get('HTTP_REFERER')
    userid = request.POST['userid']
    eventid = request.POST['eventid']
    event = Event.objects.get(id=eventid)
    user = User.objects.get(id=userid)
    if EventRegistration.objects.filter(userid=user, eventid=event).exists():
        return redirect(current_url)
    else:
        new_registration = EventRegistration.objects.create(userid=user, eventid=event)
        new_registration.save()
        return redirect(current_url)


def unregisterEvent(request):
    current_url = request.META.get('HTTP_REFERER')
    userid = request.POST['userid']
    eventid = request.POST['eventid']
    event = Event.objects.get(id=eventid)
    user = User.objects.get(id=userid)
    reg = EventRegistration.objects.get(userid=user, eventid=event)
    reg.delete()
    return redirect(current_url)

