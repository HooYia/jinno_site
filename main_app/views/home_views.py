
import logging
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import resolve, reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, View, DetailView
from django.contrib import messages
from main_app.models import HeroSection, ServicesSection, ServicesSectionTwo, Project, Testimony, Blog, SectionSettings, ContactUs, QuoteRequest, AboutStory, AboutTeam, AboutStats, AboutPartner
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

logger = logging.getLogger(__name__)

class HomePageView(TemplateView):
    template_name = 'prep/index.html'
    #template_name = 'brut/index.html'
    def get_context_data(self, **kwargs: dict[str, any]) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["hero_section"] = HeroSection.objects.first()
        context["services"] = ServicesSection.objects.all()[:3]
        context["services_two"] = ServicesSectionTwo.objects.first()
        context["projects"] = Project.objects.all().order_by('-id')[:6]
        context["testimonies"] = Testimony.objects.all().order_by('-id')[:5]
        context["blogs"] = Blog.objects.all().order_by('-id')[:3]
        completed_projects_count = Project.objects.filter(completed=True).count()
        context["completed_projects_count"] = completed_projects_count
        context["site"] = settings.SITE
        return context
    
    
    
class ServicesView(TemplateView):

    template_name = "prep/services.html"

    def get_context_data(self, **kwargs: dict[str, any]) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        context["section_settings"] = SectionSettings.objects.first()
        # cont the number of projects with completed True
        context["completed_projects_count"] = Project.objects.filter(completed=True).count()

        # Fetch all services and paginate
        services_list = ServicesSection.objects.all().order_by('-id')
        paginator = Paginator(services_list, 6)  # 6 services per page
        page = self.request.GET.get('page')
        try:
            services = paginator.page(page)
        except PageNotAnInteger:
            services = paginator.page(1)
        except EmptyPage:
            services = paginator.page(paginator.num_pages)
        
        context["services"] = services
        return context
    
    
class ServiceDetailView(DetailView):
    model = ServicesSection
    template_name = "prep/includes/service_detail.html"
    context_object_name = "service"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        context["section_settings"] = ServicesSection.objects.first()
        return context 
    
class ContactUsView(TemplateView):
    template_name = "prep/contact.html"

    def get_context_data(self, **kwargs: dict[str, any]) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        context["section_settings"] = SectionSettings.objects.first()
        return context
    
    def post(self, request: HttpRequest, *args: any, **kwargs: dict[str, any]) -> HttpResponse:
        """
        Name: post
        Description: This function handles contact form submissions with validation.
        """
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        errors = {}
        if not name:
            errors["name"] = ("Name is required.")
        if not email:
            errors["email"] = ("Email is required.")

        if errors:
            for field, msg in errors.items():
                messages.error(request, msg)
            context = self.get_context_data(**kwargs)
            context["errors"] = errors
            context["form_data"] = {
                "name": name,
                "email": email,
                "subject": subject,
                "message": message,
            }
            return render(request, self.template_name, context)

        try:
            contact_us = ContactUs.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            contact_us.save()
            messages.success(request, (_("Your message has been sent successfully.")))
            return redirect('main_app:contact')
        except Exception as e:
            messages.error(request, (_("An error occurred while sending your message. Please try again.")))
            logger.error(f"contact us error: {str(e)}")
            context = self.get_context_data(**kwargs)
            context["errors"] = errors
            context["form_data"] = {
                "name": name,
                "email": email,
                "subject": subject,
                "message": message,
            }
            return render(request, self.template_name, context)



    
class BlogView(TemplateView):
    template_name = "prep/blog.html"

    def get_context_data(self, **kwargs: dict[str, any]) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        context["section_settings"] = SectionSettings.objects.first()

        # Fetch all blogs and paginate
        blog_list = Blog.objects.all().order_by('-date')
        paginator = Paginator(blog_list, 6)  # 6 blogs per page
        page = self.request.GET.get('page')
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        
        context["blogs"] = blogs
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "prep/includes/blog_detail.html"
    context_object_name = "blog"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        context["section_settings"] = SectionSettings.objects.first()
        return context
    
    
class ProjectView(TemplateView):
    template_name = "prep/project.html"

    def get_context_data(self, **kwargs: dict[str, any]) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        context["section_settings"] = SectionSettings.objects.first()

        # Fetch all projects and paginate
        project_list = Project.objects.all().order_by('-id')
        paginator = Paginator(project_list, 6)  # 6 projects per page
        page = self.request.GET.get('page')
        try:
            projects = paginator.page(page)
        except PageNotAnInteger:
            projects = paginator.page(1)
        except EmptyPage:
            projects = paginator.page(paginator.num_pages)
        
        context["projects"] = projects
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "prep/includes/project_detail.html"
    context_object_name = "project"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        context["section_settings"] = SectionSettings.objects.first()
        return context 
    
class RequestQuoteView(View):
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get("email")
        
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')

        errors = {}
        if not first_name:
            errors['first_name'] = _("First Name is required.")
        if not last_name:
            errors['last_name'] = _("Last Name is required.")
        if not phone:
            errors['phone'] = _("Phone is required.")
        if not service:
            errors['service'] = _("Service is required.")
        if not email:
            errors['email'] = _("email is required.")
        if errors:
            for msg in errors.values():
                messages.error(request, msg)
            return redirect(request.META.get('HTTP_REFERER', 'home'))

        try:
            QuoteRequest.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                service=service,
                message=message,
                email=email,
            )
            messages.success(request, _("Your quote request has been sent successfully."))
        except Exception:
            messages.error(request, _("An error occurred while sending your quote request. Please try again."))

        return redirect(request.META.get('HTTP_REFERER', 'home'))
    
    
    
class AboutView(TemplateView):
    template_name = 'prep/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["section_settings"] = SectionSettings.objects.first()
        context["about_story"] = AboutStory.objects.first()
        context["team_members"] = AboutTeam.objects.all()
        context["about_stats"] = AboutStats.objects.first()
        context["partners"] = AboutPartner.objects.all()
        completed_projects_count = Project.objects.filter(completed=True).count()
        context["completed_projects_count"] = completed_projects_count
        return context