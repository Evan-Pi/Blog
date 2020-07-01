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

@register.filter
def get_index(queryset, item):
    list_of_ids = [i.id for i in queryset]
    index = list_of_ids.index(item.id) + 1  # +1 for pagination purposes
    return index