from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home),
    path('events/', views.events_page),   # ✅ THIS WAS MISSING
    path('event/<int:id>/', views.event_detail),

    path('add-event/', views.add_event),
    path('donate/', views.donate),

    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('register/', views.register_user),
]