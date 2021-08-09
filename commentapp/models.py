from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model): # 일대다이므로 forienkey로 연결
    article = models.ForeignKey(Article,
                                on_delete=models.SET_NULL,
                                related_name='comment',
                                null=True)
    writer = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               related_name='comment',
                               null=True)
    comment = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now=True)