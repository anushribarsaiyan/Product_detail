# yourapp/urls.py

from django.urls import path
from .views import FitTypeAPIView

urlpatterns = [
    path('fit-type/', FitTypeAPIView.as_view(), name='fit-type-api'),
]
