from django.urls import path
from . views import Register, MyLoginView, LogoutView
app_name = "users"
urlpatterns = [

    path('register/', Register.as_view(), name='register'),
    path("login/", MyLoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]