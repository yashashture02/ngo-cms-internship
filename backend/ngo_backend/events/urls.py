from django.urls import path # type: ignore
from .views import event_list
from .views import donation_list
from .views import create_event


urlpatterns = [
    path("events/", event_list, name="events"),
    path("donations/", donation_list, name="donations"),
    path("create-event/", create_event, name="create_event"),

]

