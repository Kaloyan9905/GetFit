from django.urls import path

from GetFit.web.views import IndexView, main_page

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('main/', main_page, name='main page'),
]
