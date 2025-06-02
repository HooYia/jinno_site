
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import resolve, reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = 'prep/index.html'
    #template_name = 'brut/index.html'
    def get_context_data(self, **kwargs: dict[str, any]) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
        return context
    
    
    
class ServicesView(TemplateView):

    template_name = "prep/services.html"

    def get_context_data(self, **kwargs: dict[str, any]) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["site"] = settings.SITE
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