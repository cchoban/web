from django import template
from django.conf import settings
register = template.Library()

@register.simple_tag
def site_url():
    url = settings.URL
return url
