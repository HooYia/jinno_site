
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.core.validators import RegexValidator
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
    card1_image = models.ImageField(
        upload_to='hero_cards/',
        null=True,
        blank=True,
        help_text=_("Image for the first card in the hero section")
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
    card2_image = models.ImageField(
        upload_to='hero_cards/',
        null=True,
        blank=True,
        help_text=_("Image for the second card in the hero section")
    )
    card3_title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Title for the third card in the hero section"),
    )
    card3_image = models.ImageField(
        upload_to='hero_cards/',
        null=True,
        blank=True,
        help_text=_("Image for the third card in the hero section")
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
    slug = models.SlugField(
        max_length=250,
        unique=True,
        null=True,
        blank=True,
        help_text=_("Unique slug for the service URL"),
    )

    class Meta:
        verbose_name = _("Services Section")
        verbose_name_plural = _("Services Sections")

    def __str__(self) -> str:
        return self.title or "Services Section"

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
            # Ensure uniqueness
            original_slug = self.slug
            counter = 1
            while ServicesSection.objects.filter(slug=self.slug).exclude(id=self.id).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('main_app:service_detail', kwargs={'slug': self.slug})
    
    

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
    description = RichTextField(
        blank=True,
        null=True,
        help_text=_("Detailed description of the services offered"),
    )
    projects_completed = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_("Number of projects completed"),
    )
    icon_image1 = models.ImageField(
        upload_to='services_images/',
        null=True,
        blank=True,
        help_text=_("Image for the first card in the hero section")
    )
    icon_image2 = models.ImageField(
        upload_to='services_images/',
        null=True,
        blank=True,
        help_text=_("Image for the first card in the hero section")
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
    description = RichTextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
        help_text=_("Detailed description of the project"),
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        null=True,
        blank=True,
        help_text=_("Unique slug for the project URL"),
    )
    completed = models.BooleanField(
        default=False,
        help_text=_("Indicates whether the project is completed"),
    )

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self) -> str:
        return self.title or "Project"

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
            # Ensure uniqueness
            original_slug = self.slug
            counter = 1
            while Project.objects.filter(slug=self.slug).exclude(id=self.id).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('main_app:project_detail', kwargs={'slug': self.slug})
    
    
    
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
    description = RichTextField(
        blank=True,
        null=True,
        help_text=_("The content or description of the blog post"),
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        null=True,
        blank=True,
        help_text=_("Unique slug for the blog post URL"),
    )

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self) -> str:
        return self.title or "Blog Post"

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
            # Ensure uniqueness
            original_slug = self.slug
            counter = 1
            while Blog.objects.filter(slug=self.slug).exclude(id=self.id).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('main_app:blog_detail', kwargs={'slug': self.slug})
    

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
    about_hero_section_image = models.ImageField(
        upload_to='hero_images/about/',
        null=True,
        blank=True,
        help_text=_("Hero section image for the about page"),
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
    email = models.CharField(max_length=255, null=True, blank=True)
    service = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Quote Request")
        verbose_name_plural = _("Quote Requests")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.service}"
    
    
class AboutStory(models.Model):
    story_image = models.ImageField(
        upload_to='about_images/',
        blank=True,
        null=True,
        verbose_name=_("Story Image"),
        help_text=_("Upload an image representing the company's story (e.g., office or team).")
    )
    title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("Title"),
        help_text=_("Main title for the story section (e.g., 'Building The Future Together').")
    )
    short_description = models.TextField(
        blank=True,
        verbose_name=_("Short Description"),
        help_text=_("A brief overview of the company's story.")
    )
    innovation = models.TextField(
        blank=True,
        verbose_name=_("Innovation"),
        help_text=_("Description of the company's innovation focus.")
    )
    quality = models.TextField(
        blank=True,
        verbose_name=_("Quality"),
        help_text=_("Description of the company's quality standards.")
    )
    vision = models.TextField(
        blank=True,
        verbose_name=_("Vision"),
        help_text=_("The company's vision statement.")
    )
    mission = models.TextField(
        blank=True,
        verbose_name=_("Mission"),
        help_text=_("The company's mission statement.")
    )
    values = models.TextField(
        blank=True,
        verbose_name=_("Values"),
        help_text=_("The company's core values.")
    )

    class Meta:
        verbose_name = _("About Story")
        verbose_name_plural = _("About Stories")

    def __str__(self):
        return self.title or _("About Story")
    
    
    
class AboutTeam(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Name"),
        help_text=_("Full name of the team member.")
    )
    post = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Position"),
        help_text=_("Job title or role (e.g., CEO & Founder).")
    )
    short_description = models.TextField(
        blank=True,
        verbose_name=_("Short Description"),
        help_text=_("Brief description of the team member's expertise or role.")
    )
    image = models.ImageField(
        upload_to='team_images/',
        blank=True,
        null=True,
        verbose_name=_("Profile Image"),
        help_text=_("Upload a profile image for the team member.")
    )

    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")

    def __str__(self):
        return self.name or _("Team Member")
    
    

class AboutStats(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("Title"),
        help_text=_("Title for the stats section (e.g., 'Our Impact in Numbers').")
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("Description"),
        help_text=_("Brief description of the stats section.")
    )
    projects_completed = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Projects Completed"),
        help_text=_("Number of projects completed.")
    )
    client_satisfaction = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Client Satisfaction"),
        help_text=_("Client satisfaction percentage (e.g., 98 for 98%).")
    )
    team_members = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Team Members"),
        help_text=_("Number of team members.")
    )
    countries_served = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Countries Served"),
        help_text=_("Number of countries served.")
    )

    class Meta:
        verbose_name = _("Stats")
        verbose_name_plural = _("Stats")

    def __str__(self):
        return self.title or _("Stats")
    
    
class AboutPartner(models.Model):
        logo = models.ImageField(max_length=255, blank=True, verbose_name=_("Logo URL"), help_text="URL to the partner's logo image (preferably SVG or PNG with transparent background).")

        class Meta:
            verbose_name = _("Partner")
            verbose_name_plural = _("Partners")

        def __str__(self):
            return _("Partner")
        
        

class Theme(models.Model):
    primary_color = models.CharField(
        max_length=7,
        default='#040e26',
        validators=[RegexValidator(r'^#[0-9A-Fa-f]{6}$', 'Enter a valid hex color code.')],
        help_text='Primary color in hex format (e.g., #040e26)'
    )

    secondary_color = models.CharField(
        max_length=7,
        default='#fc5e28',
        validators=[RegexValidator(r'^#[0-9A-Fa-f]{6}$', 'Enter a valid hex color code.')],
        help_text='Secondary color in hex format (e.g., #fc5e28)'
    )

    def clean(self):
        # Ensure only one instance exists
        if Theme.objects.exclude(pk=self.pk).exists() and self.pk is not None:
            raise ValidationError('Only one Theme instance is allowed.')

    def save(self, *args, **kwargs):
        # Ensure only one instance is created
        if not self.pk and Theme.objects.exists():
            raise ValidationError('Only one Theme instance can exist.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Theme with primary color {self.primary_color} and secondary color {self.secondary_color}"

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"