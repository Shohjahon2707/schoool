from django.urls import path
from apps.users.views.User.UserLogin.views import user_login_view
from apps.users.views.User.UserRegistration.views import user_register_view
urlpatterns = [
    path('login/', user_login_view,name="login"),
    path('registration/', user_register_view, name='register'),
]
