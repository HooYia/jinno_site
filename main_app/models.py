
from django.db import models
from django.utils.translation import gettext_lazy as _

class JinnoSetting(models.Model):
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
        help_text=_("The contact email address for the company"),
    )
    facebook_link = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("URL to the company's Facebook page"),
    )
    x_link = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("URL to the company's X profile"),
    )
    instagram_link = models.URLField(
        max_length=300,
        null=True,
        blank=True,
        help_text=_("URL to the company's Instagram profile"),
    )
    website_link = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("URL to the company's official website"),
    )
    company_name = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        help_text=_("The official name of the company"),
    )
    company_logo = models.ImageField(
        upload_to='company_logos/',
        null=True,
        blank=True,
        help_text=_("The company's logo image"),
    )
    slogan = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        help_text=_("The company's slogan or tagline"),
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text=_("The company's contact phone number"),
    )
    location = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("The physical address or location of the company"),
    )
    google_maps_url = models.URLField(
        max_length=600,
        null=True,
        blank=True,
        help_text=_("URL for the Google Maps embed iframe"),
    )

    def clean(self):
        # Check if another instance exists, excluding the current instance
        if self.pk is None and JinnoSetting.objects.exists():
            raise ValidationError(_("Only one JinnoSetting instance can exist."))

    def save(self, *args, **kwargs):
        # Run clean to enforce singleton
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Jinno Setting")
        verbose_name_plural = _("Jinno Settings")

    def __str__(self) -> str:
        return self.company_name or "Jinno Setting"
    

class HeroSection(models.Model):
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("The main title of the hero section"),
    )
    short_description = models.TextField(
        null=True,
        blank=True,
        help_text=_("A brief description for the hero section"),
    )
    background_image = models.ImageField(
        upload_to='hero_images/',
        null=True,
        blank=True,
        help_text=_("Background image for the hero section"),
    )
    card1_title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Title for the first card in the hero section"),
    )
    card1_description = models.TextField(
        null=True,
        blank=True,
        help_text=_("Description for the first card"),
    )
    card2_title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Title for the second card in the hero section"),
    )
    card2_description = models.TextField(
        null=True,
        blank=True,
        help_text=_("Description for the second card"),
    )
    card3_title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Title for the third card in the hero section"),
    )
    card3_description = models.TextField(
        null=True,
        blank=True,
        help_text=_("Description for the third card"),
    )
    welcome_image = models.ImageField(
        upload_to='welcome_images/',
        null=True,
        blank=True,
        help_text=_("Image for the welcome section"),
    )
    welcome_video = models.FileField(
        upload_to='welcome_videos/',
        null=True,
        blank=True,
        help_text=_("Video file for the welcome section"),
    )
    welcome_title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Title for the welcome section"),
    )
    welcome_subtitle = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Subtitle for the welcome section"),
    )
    welcome_description = models.TextField(
        null=True,
        blank=True,
        help_text=_("Detailed description for the welcome section"),
    )
    welcome_video_short_description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Short description for the welcome video"),
    )
    
    service_title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("service title"),
    )
    
    service_description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Short description for the service section"),
    )

    class Meta:
        verbose_name = _("Hero Section")
        verbose_name_plural = _("Hero Sections")

    def __str__(self) -> str:
        return self.title or "Hero Section"
    
    

class ServicesSection(models.Model):
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("The main title of the services section"),
    )
    short_description = models.TextField(
        null=True,
        blank=True,
        help_text=_("A brief description for the services section"),
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_("Detailed description of the services offered"),
    )
    image = models.ImageField(
        upload_to='services_images/',
        null=True,
        blank=True,
        help_text=_("Image representing the service"),
    )
    icon = models.ImageField(
        upload_to='services_icons/',
        null=True,
        blank=True,
        help_text=_("Icon for the service"),
    )

    class Meta:
        verbose_name = _("Services Section")
        verbose_name_plural = _("Services Sections")

    def __str__(self) -> str:
        return self.title or "Services Section"
    
    

class ServicesSectionTwo(models.Model):
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("The main title of the services section"),
    )
    short_description = models.TextField(
        null=True,
        blank=True,
        help_text=_("A brief description for the services section"),
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_("Detailed description of the services offered"),
    )
    projects_completed = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_("Number of projects completed"),
    )
    happy_customers = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_("Number of satisfied customers"),
    )
    card_image = models.ImageField(
        upload_to='services_card_images/',
        null=True,
        blank=True,
        help_text=_("Image for the service card"),
    )
   
    class Meta:
        verbose_name = _("Services Section Two")
        verbose_name_plural = _("Services Sections Two")

    def __str__(self) -> str:
        return self.title or "Services Section Two"
    
    
class Project(models.Model):
    image = models.ImageField(
        upload_to='project_images/',
        null=True,
        blank=True,
        help_text=_("Image representing the project"),
    )
    category = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Category or type of the project"),
    )
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Title of the project"),
    )
    location = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Location where the project was executed"),
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_("Detailed description of the project"),
    )

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self) -> str:
        return self.title or "Project"
    
    
    
class Testimony(models.Model):
    full_name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Full name of the person providing the testimony"),
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_("The testimonial content or description"),
    )
    image = models.ImageField(
        upload_to='testimony_images/',
        null=True,
        blank=True,
        help_text=_("Image of the person providing the testimony"),
    )
    post = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Job title or position of the person providing the testimony"),
    )

    class Meta:
        verbose_name = _("Testimony")
        verbose_name_plural = _("Testimonies")

    def __str__(self) -> str:
        return self.full_name or "Testimony"
    
    
    
class Blog(models.Model):
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("The title of the blog post"),
    )
    date = models.DateTimeField(
        null=True,
        blank=True,
        help_text=_("The publication date and time of the blog post"),
    )
    image = models.ImageField(
        upload_to='blog_images/',
        null=True,
        blank=True,
        help_text=_("Featured image for the blog post"),
    )
    author_name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("The name of the blog post author"),
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_("The content or description of the blog post"),
    )

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self) -> str:
        return self.title or "Blog Post"
    
    

class SectionSettings(models.Model):
    blog_hero_section_image = models.ImageField(
        upload_to='hero_images/blog/',
        null=True,
        blank=True,
        help_text=_("Hero section image for the blog page"),
    )
    project_hero_section_image = models.ImageField(
        upload_to='hero_images/project/',
        null=True,
        blank=True,
        help_text=_("Hero section image for the project page"),
    )
    service_hero_section_image = models.ImageField(
        upload_to='hero_images/service/',
        null=True,
        blank=True,
        help_text=_("Hero section image for the service page"),
    )
    contact_hero_section_image = models.ImageField(
        upload_to='hero_images/contact/',
        null=True,
        blank=True,
        help_text=_("Hero section image for the contact page"),
    )

    class Meta:
        verbose_name = _("Section Setting")
        verbose_name_plural = _("Section Settings")

    def __str__(self) -> str:
        return "Section Settings"
    

class ContactUs(models.Model):
    """
    Name: ContactUs  699133603
    Description: This class help to create an abstract base user.

    Author: 
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    is_answered = models.BooleanField(default=False)
    answer = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False) 
    
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"{self.name} - {self.email} - {self.subject} - {self.message} "



class Service(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text=_("The name of the service"),
    )

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self) -> str:
        return self.name
    
    
class QuoteRequest(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    service = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Quote Request")
        verbose_name_plural = _("Quote Requests")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.service}"