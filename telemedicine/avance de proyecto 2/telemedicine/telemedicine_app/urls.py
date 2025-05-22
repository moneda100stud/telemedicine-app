from django.urls import path
from .views import index, submit_data  # Import the views

urlpatterns = [
    path('', index, name='index'),  # Route for the index view
    path('submit-data', submit_data, name='submit_data'),  # Route for form submission
]
