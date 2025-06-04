from django import template
from django.contrib.auth import get_user_model
from django.http import HttpRequest

register = template.Library()
User = get_user_model()


@register.simple_tag
def compare(url, *operands):
    """
    Compare URL with one or many values.
    """
    return url in operands


@register.filter
def add_css_classes(field, css_classes):
    """
    Add CSS classes to form field
    Usage: {{ form.field|add_css_classes:"class1 class2" }}
    """
    existing_classes = field.field.widget.attrs.get("class", "")
    classes = existing_classes.split() + css_classes.split()
    unique_classes = " ".join(set(classes))  # Remove duplicates
    return field.as_widget(attrs={"class": unique_classes})


@register.filter
def no(value):
    return not value


@register.filter
def replace_language_code(request: HttpRequest, code):
    """
    Custom filter that replaces the language code in the request.path.
    """
    current_path = request.path
    # Split the URL path into parts
    path_parts = current_path.split('/', 2)

    if path_parts:
        # Replace the language code in the URL with the current language
        path_parts[1] = code if len(path_parts) > 1 else ''
        # Join the path parts back together
        new_path = '/'.join(path_parts)
        return new_path
    return current_path
