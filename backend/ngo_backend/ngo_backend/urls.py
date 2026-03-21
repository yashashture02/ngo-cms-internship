from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),        # login, logout
    path('events/', include('events.urls')),   # ✅ FIXED (VERY IMPORTANT)
]