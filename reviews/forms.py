from .models import Comments
from django import forms
from .models import Review
from django_summernote.widgets import SummernoteWidget


"""
Comment form for comments per review
"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)


"""
Review form for user to create a review
"""


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'type', 'review', 'description', 'release_year', 'fav_character', 'status')
        widgets = {
            'description': SummernoteWidget(),
            'review': SummernoteWidget()
        }