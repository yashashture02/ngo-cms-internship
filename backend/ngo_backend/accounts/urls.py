from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),

    path('dashboard/admin/', views.admin_dashboard),
    path('dashboard/staff/', views.staff_dashboard),
    path('dashboard/user/', views.user_dashboard),
]