from django.urls import path # type: ignore
from .views import event_list, create_event, donation_list, edit_event, delete_event

urlpatterns = [
    path("events/", event_list, name="events"),
    path("create-event/", create_event, name="create_event"),
    path("donations/", donation_list, name="donations"),
    path("edit-event/<int:id>/", edit_event, name="edit_event"),
    path("delete-event/<int:id>/", delete_event, name="delete_event"),
]
