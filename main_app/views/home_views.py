
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import resolve, reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from django.contrib import messages
from main_app.models import HeroSection, ServicesSection, ServicesSectionTwo, Project, Testimony, Blog, SectionSettings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

        context["site"] = settings.SITE
        return context
    
    
    
class ServicesView(TemplateView):

    template_name = "prep/services.html"

    def get_context_data(self, **kwargs: dict[str, any]) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        context["section_settings"] = SectionSettings.objects.first()

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
    
class ContactUsView(TemplateView):

    template_name = "prep/contact.html"

    def get_context_data(self, **kwargs: dict[str, any]) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context
    
    def post(self, request: HttpRequest, *args: any, **kwargs: dict[str, any]) -> HttpResponse:
        """
        Name: post

        Description: This function help to create a contact us.
        """
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact_us = ContactUs.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        contact_us.save()

        # send_email_with_html()


        messages.success(request, _("Your message has been sent successfully."))

        # context = super().get_context_data(**kwargs)
        # context["site"] = settings.SITE
        return redirect('main_app:contact')
        # return render(request, 'prep/contact.html')



def contact_us(request: HttpRequest) -> HttpResponse:
    """
    Name: contact_us

    Description: This function help to create a contact us.
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact_us = ContactUs.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        contact_us.save()

        return render(request, 'prep/contact.html')
    return render(request, 'prep/contact.html')

def contact_us_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message =  request.POST.get('message')
        
        contact_us = ContactUs.objects.create(name=name, email=email, subject=subject, message=message)
        contact_us.save()
        
        messages.success(request, 'Your message has been sent successfully.')


        # send email 
        # subject = " Contact Us "
        # message = f"Hi,{name} {email}, your message has been sent successfully."
        # from_email = settings.EMAIL_HOST_USER
        # to_email = [email]
        # send_mail(subject, message, from_email, to_email, fail_silently=False)
        
        # messages.info(request, 'Your message has been sent successfully.')

        # return redirect('main_app:contact-us')
        return render(request, 'prep/contact.html')
    else:
        return render(request, 'prep/contact.html')
    
    
    
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