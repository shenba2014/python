# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.


class QuestionModelTets(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(
            hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_now_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_questions(self):
        create_question(question_text='future question', days=2)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_questions(self):
        create_question(question_text='past question', days=-2)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['latest_question_list'][0].question_text,
            'past question')

    def test_past_future_questions(self):
        create_question(question_text='future question', days=2)
        create_question(question_text='past question', days=-2)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['latest_question_list'].count(), 1)
        self.assertEqual(
            response.context['latest_question_list'][0].question_text,
            'past question')

    def test_two_past_questions(self):
        create_question(question_text='past1 question', days=-7)
        create_question(question_text='past2 question', days=-2)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['latest_question_list'].count(), 2)
        self.assertEqual(
            response.context['latest_question_list'][0].question_text,
            'past2 question')
        self.assertEqual(
            response.context['latest_question_list'][1].question_text,
            'past1 question')


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(
            question_text='future question', days=7)
        response = self.client.get(
            reverse('polls:detail', args=(future_question.id, )))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='past question', days=-2)
        response = self.client.get(
            reverse('polls:detail', args=(past_question.id, )))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'].question_text,
                         past_question.question_text)
        self.assertContains(response, past_question.question_text)
