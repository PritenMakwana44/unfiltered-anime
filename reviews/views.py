from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review

class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-publish_date')
    template_name = 'index.html'
    paginate_by = 10
    
class ReviewDetail(View):


    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('comment_date')
        upvotes = False
        #if review.upvotes.filter(id=self.request.user.id).exists():
            #upvotes = True
        downvotes = False
        #if review.upvote.filter(id=self.request.user.id).exists():
            #downvotes = True
        
        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "upvotes": upvotes,
                "downvotes": downvotes
            },


        )