from django.urls import path,include
from .views import CustomRegisterView, GoogleLoginView, UserApiView
from allauth.socialaccount.views import signup
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView

urlpatterns = [
        # path('google/',GoogleLoginView.as_view(),name="google"),
        # path("signup/", signup, name="socialaccount_signup"),
     path("register/", CustomRegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserApiView.as_view(), name="rest_user_details"),
        ]
