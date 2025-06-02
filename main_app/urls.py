from django.urls import path
from main_app.views.home_views import HomePageView, ServicesView, ContactUsView

app_name = 'main_app'

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("services/", ServicesView.as_view(), name="services"),
    path("contact/", ContactUsView.as_view(), name="contact"),
]