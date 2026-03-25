from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home),
    path('', views.event_list),
    path('add/', views.add_event),
    path('edit-event/<int:id>/', views.edit_event),
    path('delete-event/<int:id>/', views.delete_event),
    path('donate/', views.donate),
]