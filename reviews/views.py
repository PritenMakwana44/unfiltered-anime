from django.shortcuts import render
from django.views import generic
from .models import Review

class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-publish_date')
    template_name = 'index.html'
    paginate_by = 10