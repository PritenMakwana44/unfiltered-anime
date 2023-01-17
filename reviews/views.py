from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import (CreateView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from .models import Review
from .forms import CommentForm
from .forms import ReviewForm
from django_summernote.admin import SummernoteModelAdmin
from django.urls import reverse_lazy


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-publish_date')
    template_name = 'index.html'
    paginate_by = 10

class AddReview(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ReviewForm
    template_name = 'add_review.html'
    success_url = reverse_lazy('reviews:home')

    def form_valid(self, form):
        print('USER: ', self.request.user)
        form.instance.username = self.request.user
        return super().form_valid(form)
        #return super(Review, self).form_valid(form)
    
    # def add_review(request):
    #     review_form = forms.ReviewForm()
    #     if request.method == "POST":
    #         review_form = forms.ReviewForm(request.POST)
    #         if all([review_form.is_valid()]):
    #             review_form.save()
        
    #     context = {
    #         'review_form': review_form
    #     }
    #     return render(request, 'add_review.html',context)




class ReviewDetail(View):
    model = Review
    template_name = "review_detail.html"


    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('comment_date')
        upvotes = False
        downvotes = False
        if review.upvotes.filter(id=self.request.user.id).exists():
            upvotes = True
        
        if review.downvotes.filter(id=self.request.user.id).exists():
            downvotes = True
        
        return render(
            request,
            reverse("review_detail", args=[slug]),
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
        downvotes = False
        if review.upvotes.filter(id=self.request.user.id).exists():
            upvotes = True
            downvotes = False
        if review.downvotes.filter(id=self.request.user.id).exists():
            downvotes = True
            upvotes = False
        
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.username = request.user
            comment.review_id = review
            comment.save()
            return redirect('review_detail', review.slug)
        
        else:
            return render(
                request,
                reverse("review_detail", args=[slug]),
                {
                    "review": review,
                    "comments": comments,
                    "commented": True,
                    "upvotes": upvotes,
                    "downvotes": downvotes,
                    "comment_form": comment_form,
                },
                )
class ReviewUpvotes(View):

    def post(self, request, slug):
        review = get_object_or_404(Review, slug=slug)

        if review.upvotes.filter(id=request.user.id).exists():
            review.upvotes.remove(request.user)
        else:
            review.upvotes.add(request.user)
        
        return HttpResponseRedirect(reverse('review_detail', args=[slug]))


class ReviewDownVotes(View):

    def post(self, request, slug):
        review = get_object_or_404(Review, slug=slug)

        if review.downvotes.filter(id=request.user.id).exists():
            review.downvotes.remove(request.user)
        else:
            review.downvotes.add(request.user)
        
        return HttpResponseRedirect(reverse('review_detail', args=[slug]))
