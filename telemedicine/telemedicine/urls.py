from django.contrib import admin
from django.urls import path, include  # Import the include function
from telemedicine_app.views import index # Import the index view from telemedicine_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('telemedicine_app.urls')),  # Include the URLs from the app
]
