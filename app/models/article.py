from django.db import models
from django.urls import reverse
from pytils.translit import slugify

from app.models.base import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='article_imgs', null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
    content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Жаңалық"
        verbose_name_plural = "Жаңалықтар"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:article_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1
        while Article.objects.filter(slug=slug).exists():
            slug = f'{base_slug}-{counter}'
            counter += 1
        self.slug = slug
        super().save(*args, **kwargs)
