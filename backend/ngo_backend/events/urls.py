from django.urls import path # type: ignore
from .views import event_list, add_event, create_event, donation_list, edit_event, delete_event, donate

urlpatterns = [
    path('', event_list),                  # /events/
    path('add/', add_event),              # /events/add/
    path('create-event/', create_event),
    path('donations/', donation_list),
    path('edit-event/<int:id>/', edit_event),
    path('delete-event/<int:id>/', delete_event),
    path('donate/', donate),
]