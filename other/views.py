from django.shortcuts import render
from django.http import HttpResponse

# ######:8000/other/
# Create your views here.
def simple_view(request):
    return HttpResponse("Hello, world. You're at the other index.")
