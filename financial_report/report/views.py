from django.http import HttpResponse
from django.shortcuts import render


def report_page(request):
    return HttpResponse("Сторінка звіту")


def new_record(request):
    return HttpResponse("Новий запис")
