from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('landing', views.landing_view, name="landing"),
    path('signup', views.signup_view, name="signup"),
    path('login', views.login_view, name="login"),
    path('profile', views.profile_view, name="profile"),
    path('privacy', views.privacy_view, name="privacy"),
    path('user-profile', views.user_profile_view, name="user-profile"),
    path('user-details', views.user_details_view, name="user-details"),
    path('user-preferences', views.user_preferences_view, name="user-preferences"),
    path('logout', views.logout_view, name="logout")
]
