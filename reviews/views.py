from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Review
from .forms import CommentForm

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
                "commented": False,
                "upvotes": upvotes,
                "downvotes": downvotes,
                "comment_form": CommentForm(),
            },


        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('comment_date')
        upvotes = False
        #if review.upvotes.filter(id=self.request.user.id).exists():
            #upvotes = True
        downvotes = False
        #if review.upvote.filter(id=self.request.user.id).exists():
            #downvotes = True
        
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.username = request.user
            comment.review_id = review
            comment.save()
            return redirect('review_detail', review.slug)
        
        else:
            # comment_form()
            return render(
                request,
                "review_detail.html",
                {
                    "review": review,
                    "comments": comments,
                    "commented": True,
                    "upvotes": upvotes,
                    "downvotes": downvotes,
                    # "comment_form": CommentForm(),
                    "comment_form": comment_form,
                },


        )