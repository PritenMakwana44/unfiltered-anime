from .models import Comments
from django import forms
from .models import Review
from django_summernote.widgets import SummernoteWidget



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ('slug','upvotes', 'downvotes',)
        widgets = {
            'description': SummernoteWidget(),
            'review': SummernoteWidget()
        }