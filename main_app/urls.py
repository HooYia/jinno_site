from django.urls import path
from main_app.views.home_views import BlogDetailView, HomePageView, ProjectDetailView, ServicesView, ContactUsView, BlogView, ProjectView, RequestQuoteView, AboutView

app_name = 'main_app'

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("services/", ServicesView.as_view(), name="services"),
    path("contact/", ContactUsView.as_view(), name="contact"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("projects/", ProjectView.as_view(), name="projects"),
    path("request-quote/", RequestQuoteView.as_view(), name="request_quote"),
    path("about/", AboutView.as_view(), name="about"),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail')




]