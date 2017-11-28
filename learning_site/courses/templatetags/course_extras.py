from django import template
from ..models import Course


register = template.Library()

@register.simple_tag
def newest_course():
    '''Get's the most recent course added to lib.'''
    return Course.objects.latest('created_at')


@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    '''Returns dict of courses to display'''
    return {'courses': Course.objects.all()}
