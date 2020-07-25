from django.db import models
from django.utils import timezone

from account.models import RedUser

class PraiseMePost(models.Model):
    author = models.ForeignKey(RedUser, related_name='praiseAuthor', on_delete=models.CASCADE, null=False, blank=False, verbose_name="작성자")
    put_date = models.DateTimeField(verbose_name="게시일")
    body = models.TextField()

class praiseMeComment(models.Model):
    author =  models.ForeignKey(RedUser, related_name='praiseMeCommentAuthor', on_delete=models.CASCADE, null=False, blank=False, verbose_name="댓글 작성자")
    post = models.ForeignKey('praiseMeApp.PraiseMePost', on_delete=models.CASCADE, related_name = 'praiseMeCommentTargetPost')
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)