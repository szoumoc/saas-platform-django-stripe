import pathlib
from django.shortcuts import render
from django.http import HttpResponse, request

from visits.models import PageVisit 

this_dir = pathlib.Path(__file__).resolve().parent
def home_page_view(request, *args, **kwargs ):
    return about_page_view(request, *args, **kwargs)

def about_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path)
    my_title = "My page"
    html_template = "home.html"
    my_context = {
        "page_title": my_title,
        "page_visit_count": qs.count(),
        "total_visit_count": page_qs.count()
    }
    path = request.path
    
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)