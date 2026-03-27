from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('events.urls')),     # homepage + events
    path('', include('accounts.urls')),   # login/dashboard
]