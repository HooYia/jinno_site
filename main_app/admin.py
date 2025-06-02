from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import (
    JinnoSetting, HeroSection, ServicesSection, ServicesSectionTwo,
    Project, Testimony, Blog, SectionSettings
)

@admin.register(JinnoSetting)
class JinnoSettingAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone_number', 'location')
    search_fields = ('company_name', 'email', 'phone_number', 'location')
    fieldsets = (
        (None, {
            'fields': ('company_name', 'slogan', 'company_logo')
        }),
        (_('Contact Information'), {
            'fields': ('email', 'phone_number', 'location')
        }),
        (_('Social Media'), {
            'fields': ('facebook_link', 'x_link', 'instagram_link', 'website_link')
        }),
    )

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'welcome_title', 'service_title')
    search_fields = ('title', 'welcome_title', 'service_title', 'short_description')
    fieldsets = (
        (_('Main Hero Content'), {
            'fields': ('title', 'short_description', 'background_image')
        }),
        (_('Card 1'), {
            'fields': ('card1_title', 'card1_description')
        }),
        (_('Card 2'), {
            'fields': ('card2_title', 'card2_description')
        }),
        (_('Card 3'), {
            'fields': ('card3_title', 'card3_description')
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
    list_filter = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'description', 'image', 'icon')
        }),
    )

@admin.register(ServicesSectionTwo)
class ServicesSectionTwoAdmin(admin.ModelAdmin):
    list_display = ('title', 'projects_completed', 'happy_customers')
    search_fields = ('title', 'short_description', 'description')
    list_filter = ('projects_completed', 'happy_customers')
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'description', 'projects_completed', 'happy_customers', 'card_image')
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location')
    search_fields = ('title', 'category', 'location', 'description')
    list_filter = ('category',)
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'location', 'description', 'image')
        }),
    )

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'post')
    search_fields = ('full_name', 'post', 'description')
    fieldsets = (
        (None, {
            'fields': ('full_name', 'post', 'description', 'image')
        }),
    )

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'date')
    search_fields = ('title', 'author_name', 'description')
    list_filter = ('date',)
    date_hierarchy = 'date'
    fieldsets = (
        (None, {
            'fields': ('title', 'author_name', 'date', 'description', 'image')
        }),
    )

@admin.register(SectionSettings)
class SectionSettingsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    fieldsets = (
        (None, {
            'fields': (
                'blog_hero_section_image',
                'project_hero_section_image',
                'service_hero_section_image',
                'contact_hero_section_image'
            )
        }),
    )