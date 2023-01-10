from django.shortcuts import render
from django.views import generic
from .models import Review


class HomeView(requests):
    model = Home
    template_name = 'index.html'



class ReviewList(generic.ListView):
    model = Reviews
    queryset = Review.objects.filter(status=1).order_by('-publish_date')
    template_name = 'review.html'
    paginate_by = 10
    
