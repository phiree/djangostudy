import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from polls.models import Poll
# Create your tests here.
class PollMethoedTests(TestCase):
    def test_was_published_recently_with_future_pull(self):
        '''
        was_published_recently should return False for polls
        whose pub_date is in the future
        '''
        future_poll=Poll(pub_date=timezone.now()+datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)
        
    def test_was_published_recently_with_old_poll(self):
        future_poll=Poll(pub_date=timezone.now()-datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)
        
    def test_was_published_recently_with_rencet_poll(self):
        future_poll=Poll(pub_date=timezone.now()-datetime.timedelta(hours=1))
        self.assertEqual(future_poll.was_published_recently(), True)

def create_poll(question,days):
    '''create a poll with the given question and published the given number 
    of days offset to new(negative for polls published in the past,positive
    for the polls tat have yet to be published'''   
    return Poll.objects.create(question=question
                               ,pub_date=timezone.now()+datetime.timedelta(days=days))
        
class PollViewTests(TestCase):
    def test_indexView_with_no_polls(self):
        '''If no polls exist, an appropriate message should be displayed'''      
        response=self.client.get(reverse("polls:index"))
        print (response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No")
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])
    def test_indexView_with_a_future_poll(self):
        poll=create_poll('q1',30)
        response=self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context['latest_poll_list'],[])
    def test_indexView_with_a_past_poll(self):
        poll=create_poll('q1',-30)
        response=self.client.get(reverse("polls:index"))
        self.assertEqual(list(response.context['latest_poll_list']),[poll])

class PollDetailtests(TestCase):
    def test_detail_view_with_a_future_poll(self):
        future_poll=create_poll('FP',20)
        response=self.client.get(reverse("polls:detail",args=(future_poll.id,)))
        self.assertEqual(response.status_code,404)
    def test_detail_view_with_a_recent_poll(self):
        recent_poll=create_poll('RP',-1)
        print(recent_poll.id)
        response=self.client.get(reverse("polls:detail",args=(recent_poll.id,)))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,recent_poll)
        
