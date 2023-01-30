from django.test import TestCase
from.forms import CommentForm, ReviewForm

class TestCommentForm(TestCase):

    def test_item_name_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = CommentForm({'body': 'Test comment'})
        self.assertTrue(form.is_valid())

