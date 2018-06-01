from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def CricketCenterIndexView(request):
    return render(request, "cricket_center/cricket_center_index.html",)
