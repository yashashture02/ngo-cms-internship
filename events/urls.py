from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),                # homepage
    path('events/', views.event_list),  # list
    path('add/', views.add_event),      # add
    path('edit/<int:id>/', views.edit_event),
    path('delete/<int:id>/', views.delete_event),
    path('donate/', views.donate),      # donate
]