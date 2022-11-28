from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


def user_directory_path(instance, filename):
    return 'posts/%Y/%m/%d/'.format(instance.id, filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    text_introduction = models.TextField(null=True)
    image = models.ImageField(
        upload_to='images/posts', default='posts/default.jpg')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    text_location = models.TextField(null=True)
    image_location = models.ImageField(
        upload_to='images/posts', default='posts/default.jpg')
    text_weight = models.TextField(null=True)
    text_size = models.TextField(null=True)
    text_class = models.TextField(null=True)
    text_order = models.TextField(null=True)
    text_family = models.TextField(null=True)

    image_2 = models.ImageField(
        upload_to='images/posts', default='posts/default.jpg')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    def get_absolute_url(self):
        return reverse('blog:post_single', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(MPTTModel):

    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['publish']

    def __str__(self):
        return self.name

	


class Carousel(models.Model):
    Image = models.ImageField(upload_to='Carousel', null = True)
    Img_title = models.CharField(max_length=30, null=True)
    Img_desc = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Img_title