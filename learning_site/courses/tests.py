from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone
from time import sleep

from .models import Course, Step

class CourseModelTests(TestCase):
    def test_course_creations(self):
        course = Course.objects.create(
            title="Python regular expressions",
            description="Learn to write regex's in Python"
        )
        sleep(0.001)
        now = timezone.now()
        self.assertLess(course.created_at, now)


class StepModelTests(TestCase):
    def test_default_content(self):
        step = Step.objects.create(
            title="Named groups",
            description="Name your regex groups",
            #content omitted
            order=0,
            course=Course.objects.create()
        )
        self.assertEqual(step.content, '')

    def test_default_order(self):
        step = Step.objects.create(
            title="Named groups",
            description="Name your regex groups",
            content="blah, blah, blah",
            # order omitted
            course=Course.objects.create()
        )
        self.assertEqual(step.order, 0)


class CourseViewsTests(TestCase):
    # creates a temporary test db with only the given objects
    # note they are created in order (for pk)
    def setUp(self):
        self.course1 = Course.objects.create(
            title='Python Testing',
            description="Learn to write tests in Python"
        )
        self.course2 = Course.objects.create(
            title='New Course',
            description='A new course'
        )
        self.step = Step.objects.create(
            title='Intro to Doctests',
            description='Learn to write tests in docstrings',
            course=self.course1
        )

    def test_course_list_view(self):
        response = self.client.get(reverse('courses:list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.course1, response.context['courses'])
        self.assertIn(self.course2, response.context['courses'])
        self.assertTemplateUsed(response, 'courses/course_list.html')
        self.assertContains(response, self.course1.title)

    def test_course1_detail_view(self):
        response = self.client.get(reverse(
            'courses:detail', kwargs={'pk':self.course1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.course1, response.context['course'])
        self.assertTemplateUsed(response, 'courses/course_detail.html')
        self.assertContains(response, self.course1.description)

    def test_course2_detail_view(self):
        response = self.client.get(reverse(
            'courses:detail', kwargs={'pk':self.course2.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.course2, response.context['course'])
        self.assertTemplateUsed(response, 'courses/course_detail.html')
        self.assertContains(response, self.course2.description)

    def test_step_detail_view(self):
        response = self.client.get(reverse(
            'courses:step',
            kwargs={
                'course_pk':self.course1.pk,
                'step_pk':self.step.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.step, response.context['step'])
        self.assertEqual(self.course1, response.context['step'].course)
        self.assertTemplateUsed(response, 'courses/step_detail.html')
        self.assertContains(response, self.step.title)
        self.assertContains(response, self.step.content)
        self.assertNotContains(response, self.step.description)
