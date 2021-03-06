# urls.py
from django.urls import path
from codershq.hackathon.views import HackathonList, HackathonDetail

app_name = "hackathon"
urlpatterns = [
    path('', HackathonList.as_view(), name="list"),
    path('<slug:slug>/', HackathonDetail.as_view(), name="detail"),
]