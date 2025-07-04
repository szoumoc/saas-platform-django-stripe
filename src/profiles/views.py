from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import get_user_model


User = get_user_model()
@login_required
def profile_view(request, username=None, *args, **kwargs):
    user = request.user
    print('user.has_perm("auth.view_user")', user.has_perm("auth.view_user"))
    profile_user_obj = get_object_or_404(User, username=username)
    print(profile_user_obj)
    print(user)
    is_me = profile_user_obj == user
    return HttpResponse(f"Profile View for {profile_user_obj.id}, is_me: {is_me}")