from django import template
from django.utils.safestring import mark_safe
from ..models import Course
import markdown2


register = template.Library()

@register.simple_tag
def newest_course():
    '''Get's the most recent course added to lib.'''
    return Course.objects.latest('created_at')


@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    '''Returns dict of courses to display'''
    return {'courses': Course.objects.all()}


@register.filter
def time_estimate(word_count):
    '''Estimates number of minutes to complete a step.'''
    return round(word_count / 20)


@register.filter('md_to_html')
def md_to_html(md_txt):
    return mark_safe(markdown2.markdown(md_txt))
