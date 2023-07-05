from django.urls import path

from GetFit.web.views import IndexView, login

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('login/', login, name='login'),
)
