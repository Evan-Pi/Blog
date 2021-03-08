from django import template
from django.utils.text import slugify
from unidecode import unidecode
from django.utils.timezone import localtime, now
register = template.Library()

@register.filter
def unidecode_and_slugify(slug):

    unicode_slug = slugify(unidecode(slug))

    return unicode_slug

@register.simple_tag
def my_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0]!=field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)

    return url

import random

@register.simple_tag
def random_background_color():
    colors = ['#49443d','#c1a188','#f9e3d7','#8ca18e','#7d9396','#38483e','#61846f','#4d6858','#786147','#9e9580']
    return random.choice(colors)