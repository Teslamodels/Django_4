from django.urls import path
from .views import you, tube

urlpatterns = [
    path('', you.as_view(), name='You'),
    path('youtube/', tube.as_view(), name='Tube'),
]