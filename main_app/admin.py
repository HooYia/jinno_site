
import logging

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import (
    JinnoSetting, HeroSection, ServicesSection, ServicesSectionTwo,
    Project, Testimony, Blog, SectionSettings, ContactUs, Service, 
    QuoteRequest, AboutStory, AboutTeam, AboutStats, AboutPartner, Theme
)


logger = logging.getLogger(__name__)


@admin.register(JinnoSetting)
class JinnoSettingAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone_number', 'location', 'google_maps_url')
    search_fields = ('company_name', 'email', 'phone_number', 'location', 'google_maps_url')
    list_filter = ('company_name', 'location')
    fieldsets = (
        (None, {
            'fields': ('company_name', 'slogan', 'company_logo')
        }),
        (_('Contact Information'), {
            'fields': ('email', 'phone_number', 'location', 'google_maps_url')
        }),
        (_('Social Media'), {
            'fields': ('facebook_link', 'x_link', 'instagram_link', 'website_link')
        }),
    )

    def has_add_permission(self, request):
        return not JinnoSetting.objects.exists()

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'welcome_title', 'service_title')
    search_fields = ('title', 'welcome_title', 'service_title', 'short_description')
    list_filter = ('title', 'welcome_title')
    fieldsets = (
        (_('Main Hero Content'), {
            'fields': ('title', 'short_description', 'background_image')
        }),
        (_('Card 1'), {
            'fields': ('card1_title', 'card1_description', 'card1_image')
        }),
        (_('Card 2'), {
            'fields': ('card2_title', 'card2_description', 'card2_image')
        }),
        (_('Card 3'), {
            'fields': ('card3_title', 'card3_description', 'card3_image')
        }),
        (_('Welcome Section'), {
            'fields': ('welcome_title', 'welcome_subtitle', 'welcome_description', 'welcome_image', 'welcome_video', 'welcome_video_short_description')
        }),
        (_('Service Section'), {
            'fields': ('service_title', 'service_description')
        }),
    )

@admin.register(ServicesSection)
class ServicesSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'short_description', 'description')
    list_filter = ('title', 'icon')
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'description', 'image', 'icon')
        }),
    )

@admin.register(ServicesSectionTwo)
class ServicesSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'projects_completed', 'happy_customers')
    search_fields = ('title', 'short_description', 'description')
    list_filter = ('projects_completed', 'happy_customers')
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'description', 'projects_completed', 'happy_customers', 'card_image', 'icon_image1', 'icon_image2')
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'slug', 'completed')
    search_fields = ('title', 'category', 'location', 'description', 'slug', 'completed')
    list_filter = ('category', 'location', 'completed')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'location', 'description', 'image', 'completed')
        }),
    )

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'date', 'slug')
    search_fields = ('title', 'author_name', 'description', 'slug')
    list_filter = ('date', 'author_name')
    date_hierarchy = 'date'
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author_name', 'date', 'description', 'image')
        }),
    )
@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'post')
    search_fields = ('full_name', 'post', 'description')
    list_filter = ('post',)
    fieldsets = (
        (None, {
            'fields': ('full_name', 'post', 'description', 'image')
        }),
    )

@admin.register(SectionSettings)
class SectionSettingsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = (
        'blog_hero_section_image__url',
        'project_hero_section_image__url',
        'service_hero_section_image__url',
        'contact_hero_section_image__url',
        'about_hero_section_image__url',
    )
    list_filter = (
        'blog_hero_section_image',
        'project_hero_section_image',
        'service_hero_section_image',
        'contact_hero_section_image',
        'about_hero_section_image',
    )
    fieldsets = (
        (None, {
            'fields': (
                'blog_hero_section_image',
                'project_hero_section_image',
                'service_hero_section_image',
                'contact_hero_section_image',
                'about_hero_section_image',
            )
        }),
    )

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'is_answered', 'create_at', 'is_deleted')
    list_filter = ('is_read', 'is_answered', 'is_deleted', 'create_at')
    search_fields = ('name', 'email', 'subject', 'message', 'answer')
    readonly_fields = ('create_at',)
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Admin Actions', {
            'fields': ('is_read', 'is_answered', 'answer', 'is_deleted'),
        }),
        ('Metadata', {
            'fields': ('create_at',),
            'classes': ('collapse',),
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'service', 'phone', 'created_at')
    list_filter = ('service', 'created_at')
    search_fields = ('first_name', 'last_name', 'service', 'phone', 'message')
    readonly_fields = ('created_at',)
    fieldsets = (
        ("Client Information", {
            'fields': ('first_name', 'last_name', 'phone')
        }),
        ("Service Details", {
            'fields': ('service', 'message')
        }),
        ("Metadata", {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    ordering = ('-created_at',)



@admin.register(AboutStory)
class AboutStoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'short_description', 'innovation', 'quality', 'vision', 'mission', 'values')
    list_filter = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'story_image')
        }),
        (_('Core Values'), {
            'fields': ('innovation', 'quality')
        }),
        (_('Mission & Vision'), {
            'fields': ('mission', 'vision', 'values')
        }),
    )

@admin.register(AboutTeam)
class AboutTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')
    search_fields = ('name', 'post', 'short_description')
    list_filter = ('post',)
    fieldsets = (
        (None, {
            'fields': ('name', 'post', 'short_description', 'image')
        }),
    )

@admin.register(AboutStats)
class AboutStatsAdmin(admin.ModelAdmin):
    list_display = ('title', 'projects_completed', 'client_satisfaction', 'team_members', 'countries_served')
    search_fields = ('title', 'description')
    list_filter = ('projects_completed', 'client_satisfaction')
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        (_('Metrics'), {
            'fields': ('projects_completed', 'client_satisfaction', 'team_members', 'countries_served')
        }),
    )

@admin.register(AboutPartner)
class AboutPartnerAdmin(admin.ModelAdmin):
    list_display = ('logo',)
    search_fields = ('logo',)
    fieldsets = (
        (None, {
            'fields': ('logo',)
        }),
    )

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['primary_color', 'secondary_color']
    fields = ['primary_color', 'secondary_color']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['primary_color'].widget.attrs['type'] = 'color'  # HTML5 color picker
        form.base_fields['secondary_color'].widget.attrs['type'] = 'color'  # HTML5 color picker
        return form

    def has_add_permission(self, request):
        # Prevent adding new instances if one exists
        return not Theme.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deleting the singleton instance
        return False

    def get_queryset(self, request):
        # Ensure the singleton is always available
        qs = super().get_queryset(request)
        return qs

    def save_model(self, request, obj, form, change):
        # Ensure the singleton is saved correctly
        if not Theme.objects.exists():
            obj.save()
        else:
            # Update the existing instance
            existing = Theme.objects.first()
            existing.primary_color = obj.primary_color
            existing.secondary_color = obj.secondary_color
            existing.save()
    
admin.site.site_header = _("JINOO ADMIN")
admin.site.site_title = _("JINOO ADMIN PORTAL")
admin.site.index_title = _("WELCOME TO JINOO ADMIN PORTAL")