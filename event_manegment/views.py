from django.shortcuts import render, redirect, get_object_or_404
from events.models import Event, Category
from django.contrib import messages


def home(request):
    events = Event.objects.all()
    return render(request, 'main/home.html', {'events': events})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'main/event_list.html', {'events': events})


def event_detail(request, pk):
    events = Event.objects.filter(pk=pk)
    category = Category.objects.all()
    contex = {
        'events': events,
        'category': category
    }
    return render(request, 'main/event_detail.html', contex)


def add_event(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('eventName')
        category_id = request.POST.get('eventCategory')
        start_date = request.POST.get('eventStartDate')
        start_time = request.POST.get('eventStartTime')
        end_date = request.POST.get('eventEndDate')
        end_time = request.POST.get('eventEndTime')
        priority = request.POST.get('priority')
        description = request.POST.get('eventDescription')
        location = request.POST.get('eventLocation')
        organizer = request.POST.get('eventOrganizer')

        try:
            start_datetime = f"{start_date} {start_time}"
            end_datetime = f"{end_date} {end_time}"

            category = Category.objects.get(id=category_id)

            add_data = Event(
                name=name,
                category=category,
                start_date=start_datetime,
                end_date=end_datetime,
                priority=priority,
                description=description,
                location=location,
                organizer=organizer
            )
            add_data.save()
            messages.success(request, 'Event added successfully!')
            return redirect('event_list')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('add_event')
    return render(request, 'main/event_form.html', {'categories': categories})


def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    categories = Category.objects.all()
    contex = {
        'event': event,
        'categories': categories,
    }
    if request.method == 'POST':
        name = request.POST.get('eventName')
        category_id = request.POST.get('eventCategory')
        start_date = request.POST.get('eventStartDate')
        start_time = request.POST.get('eventStartTime')
        end_date = request.POST.get('eventEndDate')
        end_time = request.POST.get('eventEndTime')
        priority = request.POST.get('priority')
        description = request.POST.get('eventDescription')
        location = request.POST.get('eventLocation')
        organizer = request.POST.get('eventOrganizer')

        try:
            start_datetime = f"{start_date} {start_time}"
            end_datetime = f"{end_date} {end_time}"

            event.name = name
            event.category = Category.objects.get(id=category_id)
            event.start_date = start_datetime
            event.end_date = end_datetime
            event.priority = priority
            event.description = description
            event.location = location
            event.organizer = organizer
            event.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_list')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
    return render(request, 'main/event_update_form.html', contex)


def delete_event(request, pk):
    event = Event.objects.get(pk=pk)
    event.delete()
    return redirect('event_list')
    # return render(request, 'main/event_confirm_delete.html', {'event': event})


def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('categoryName')
        try:
            add_category = Category(name=name, )
            add_category.save()
            messages.success(request, 'Category added successfully!')
            return redirect('category_list')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('create_category')
    return render(request, 'main/create_category.html')


def category_list(request):
    categories = Category.objects.all()
    contex = {
        'categories': categories,
    }
    return render(request, 'main/category_list.html', contex)


def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    messages.warning(request, 'Category deleted successfully!')
    return redirect('category_list')


def guest_event_list(request):
    events = Event.objects.all()
    return render(request, 'guest/guest_event_list.html', {'events': events})


def guest_event_details(request,pk):
    category = Category.objects.all()
    events = Event.objects.all()
    contex = {
        'category': category,
        'events': events
    }
    return render(request, 'guest/guest_event_details.html', contex)
