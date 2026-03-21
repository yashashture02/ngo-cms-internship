from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('dashboard/', views.dashboard),
]