from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('events/', views.events_page),
    path('event/<int:id>/', views.event_detail),

    path('add-event/', views.add_event),
    path('edit-event/<int:id>/', views.edit_event),  # 🔥 IMPORTANT
    path('delete-event/<int:id>/', views.delete_event),  # 🔥 NEW

    path('donate/', views.donate),

    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('register/', views.register_user),
]