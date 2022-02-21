from django import template
from django.template.loader import get_template
from posts.models import Post, Category
import re , os 
register = template.Library()

@register.simple_tag(takes_context=True)
def recent_posts(context):
    return Post.objects.all().order_by('-created_at')[0:5]

@register.simple_tag(takes_context=True)
def get_categories(context):
    # only show for 6 categories 
    return Category.objects.all()[0:6]
    
@register.simple_tag(takes_context=True)
def all_categories(contest):
    return Category.objects.all()

@register.filter(name='short_description')
def short_description(value, l=200):
    return ' '.join(re.findall('<p>([\w\d\s\,\.\-]+)</p>', value))[0:int(l)]

@register.filter(name='is_exists')
def is_exists(value):
    if value and os.path.exists(value.path):
        return True 