from django.urls import path

from .views import report_page, new_record

urlpatterns = [
    path('', report_page),
    path('new_record/', new_record),
]