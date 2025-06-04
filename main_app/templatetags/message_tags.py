from django import template

register = template.Library()

@register.filter
def bootstrap_class(tag):
    mapping = {
        'alert-debug': 'secondary',
        'alert-info': 'info',
        'alert-success': 'success',
        'alert-warning': 'warning',
        'alert-danger': 'danger',
    }
    return mapping.get(tag, 'secondary')

