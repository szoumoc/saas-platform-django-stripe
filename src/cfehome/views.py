import pathlib
from django.shortcuts import render, redirect
from django.http import HttpResponse
from visits.models import PageVisit 
# views.py
from django.http import JsonResponse




this_dir = pathlib.Path(__file__).resolve().parent
def home_page_view(request, *args, **kwargs ):
    if request.user.is_authenticated:
        print(request.user.first_name)
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
VALID_CODE = "abc123"
def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get('protected_page_allowed') or 0
    # print(request.session.get('protected_page_allowed'), type(request.session.get('protected_page_allowed')))
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            is_allowed = 1
            request.session['protected_page_allowed'] = is_allowed
    if is_allowed:
        return render(request, "protected/view.html", {})
    return render(request, "protected/entry.html", {})