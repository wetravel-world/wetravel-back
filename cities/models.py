from django.conf import settings
from django.db import models
from django.utils.text import slugify


CONTINENTS = [
    ('Africa', 'Africa'),
    ('Americas', 'Americas'),
    ('Asia', 'Asia'),
    ('Europe', 'Europe'),
    ('Middle East', 'Middle East'),
    ('Oceania', 'Oceania'),
]


class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    continent = models.CharField(max_length=20, choices=CONTINENTS, default='Europe', db_index=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    welcome_score = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    score_count = models.PositiveIntegerField(default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    hero_image_url = models.URLField(blank=True, max_length=1000)
    hero_image_attribution_name = models.CharField(max_length=200, blank=True)
    hero_image_attribution_url = models.URLField(blank=True)
    meta_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'cities'
        ordering = ['-welcome_score', 'name']

    def __str__(self):
        return f'{self.name}, {self.country}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.country}')
        super().save(*args, **kwargs)


class Place(models.Model):
    city = models.ForeignKey(City, related_name='places', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    place_type = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, max_length=1000)
    google_place_id = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.city.name})'


class Comment(models.Model):
    city = models.ForeignKey(City, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    score = models.PositiveSmallIntegerField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.author} on {self.city.name} (score={self.score})'


class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Reply by {self.author} on comment {self.comment_id}'
