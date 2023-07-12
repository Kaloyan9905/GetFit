from django.urls import path
from GetFit.auth_user.views import SignInView, SignUpView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
)
