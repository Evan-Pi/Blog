from django import template
from django.utils.text import slugify
from unidecode import unidecode
register = template.Library()

@register.filter
def unidecode_and_slugify(slug):

    unicode_slug = slugify(unidecode(slug))

    return unicode_slug