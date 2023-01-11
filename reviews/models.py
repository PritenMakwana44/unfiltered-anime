from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
ANIME_TYPE = [
    ('FILM', 'Film'),
    ('SHOW', 'Show')
]

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Review_page")
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.CharField(max_length=4, choices=ANIME_TYPE, default='Film')
    featured_image = CloudinaryField('image', default='placeholder')
    release_year = models.PositiveSmallIntegerField()
    publish_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=300)
    review = models.CharField(max_length=300, unique=True)
    fav_character = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS, default=0)
    upvotes = models.ManyToManyField(
        User, related_name='review_upvote', blank=True)
    downvotes = models.ManyToManyField(
        User, related_name='review_downvote', blank=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def number_of_upvotes(self):
        return self.upvotes.count()

    def number_of_downvotes(self):
        return self.downvotes.count()


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["comment_date"]

    def __str__(self):
        return f"Comment {self.body} by {self.username}"


class WatchLater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlater")
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="watchlater")
