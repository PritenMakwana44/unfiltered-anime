from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import (CreateView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from .models import Review, Comments
from .models import WatchLater
from .forms import CommentForm
from .forms import ReviewForm
from django_summernote.admin import SummernoteModelAdmin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-publish_date')
    template_name = 'index.html'
    paginate_by = 10


class AddReview(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ReviewForm
    template_name = 'add_review.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print('USER: ', self.request.user)
        form.instance.username = self.request.user
        return super().form_valid(form)

"""
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
                "review_detail.html",
                {
                    "review": review,
                    "comments": comments,
                    "commented": True,
                    "upvotes": upvotes,
                    "downvotes": downvotes,
                    "comment_form": comment_form,
                },
                )

"""

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
            "review_detail.html",

            {
                "review": review,
                "comments": comments,
                "commented": False,
                "upvotes": upvotes,
                "downvotes": downvotes,
                "comment_form": CommentForm(),
                "is_staff": request.user.is_staff,
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
                "review_detail.html",
                {
                    "review": review,
                    "comments": comments,
                    "commented": True,
                    "upvotes": upvotes,
                    "downvotes": downvotes,
                    "comment_form": comment_form,
                    "is_staff": request.user.is_staff,
                },
            )

class DeleteCommentView(View):
    def post(self, request, comment_id, *args, **kwargs):
        comment = Comments.objects.get(comment_id=comment_id)
        comment.delete()
        return redirect('review_detail', comment.review_id.slug)



class ReviewUpvotes(View):
    def post(self, request, slug):
        review = get_object_or_404(Review, slug=slug)
        if review.downvotes.filter(id=request.user.id).exists():
            review.downvotes.remove(request.user)
        if review.upvotes.filter(id=request.user.id).exists():
            review.upvotes.remove(request.user)
        else:
            review.upvotes.add(request.user)

        return HttpResponseRedirect(reverse('review_detail', args=[slug]))


class ReviewDownVotes(View):

    def post(self, request, slug):
        review = get_object_or_404(Review, slug=slug)
        if review.upvotes.filter(id=request.user.id).exists():
            review.upvotes.remove(request.user)
        if review.downvotes.filter(id=request.user.id).exists():
            review.downvotes.remove(request.user)
        else:
            review.downvotes.add(request.user)

        return HttpResponseRedirect(reverse('review_detail', args=[slug]))


@login_required
def review_edit(request, slug):
    review = get_object_or_404(Review, slug=slug)
    if request.user != review.username:
        messages.error(request, 'Sorry, only the author can edit this review')
        return redirect(reverse_lazy('home'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated!')
            return redirect(reverse('review_detail', args=[slug]))
        else:
            messages.error(request,
                           ('Please ensure the form is valid.'))
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {review.title}')
        template = 'edit_review.html'
        context = {
            'form': form,
            'review': review,
        }
        return render(request, template, context)

"""
@login_required
def delete_review(request, slug):
    review = get_object_or_404(Review, slug=slug)
    if request.user != review.username:
        messages.error(request,
                       "You are not authorized to delete this review.")
        return redirect('review_detail', review.slug)
    review.delete()
    messages.success(request, "Review deleted successfully.")
    return redirect('home')
"""

@login_required
def delete_review(request, slug):
    review = get_object_or_404(Review, slug=slug)
    if not request.user.is_staff and request.user != review.username:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect('review_detail', review.slug)
    review.delete()
    messages.success(request, "Review deleted successfully.")
    return redirect('home')

@login_required
def add_to_watch_later(request, review_id):
    if request.user.is_authenticated:
        # check if the review has already been added
        existing_watch_later = WatchLater.objects.filter(review_id=review_id,
                                                         username=request.user)
        if existing_watch_later.exists():
            messages.error(request, "Already added to Watch list!")
            # the review has already been added

            return redirect('home')  # or some other appropriate response

        watch_later = WatchLater()
        watch_later.review_id = Review.objects.get(review_id=review_id)
        watch_later.username = request.user
        watch_later.save()
        return redirect('home')
    else:
        messages.success(request, "Please login!")
        return redirect('login')


def watch_later_list(request):
    watch_later_list = WatchLater.objects.filter(username=request.user)
    return render(request, 'watch_later/watch_later_list.html',
                  {'watch_later_list': watch_later_list})


@login_required
def remove_from_watch_later(request, watch_id):
    if request.user.is_authenticated:
        instance = WatchLater.objects.filter(watch_id=watch_id)
        instance.delete()
        messages.success(request, "Removed from your watch later list!")

        return redirect('home')  # or some other appropriate response

    else:
        messages.success(request, "Please login!")
        return redirect('login')



