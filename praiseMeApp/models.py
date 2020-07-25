from django.db import models
from django.utils import timezone

class PraiseMePost(models.Model):
    author = models.ForeignKey('account.Donator', related_name='donatorPraiseAuthor', on_delete=models.CASCADE, null=False, blank=False, verbose_name="수여자")
    put_date = models.DateTimeField(verbose_name="게시일")
    body = models.TextField()

class ReceiverPraiseMeComment(models.Model):
    author =  models.ForeignKey('account.Receiver', related_name='PrasieMeAuthorReceiver', on_delete=models.CASCADE, null=False, blank=False, verbose_name="댓글 작성 수여자")
    post = models.ForeignKey('praiseMeApp.PraiseMePost', on_delete=models.CASCADE, related_name = 'ReceiverPraiseComment')
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

class DonatorPraiseMeComment(models.Model):
    author =  models.ForeignKey('account.Donator', related_name='PrasieMeAuthorDonator', on_delete=models.CASCADE, null=False, blank=False, verbose_name="댓글 작성 헌혈자")
    post = models.ForeignKey('praiseMeApp.PraiseMePost', on_delete=models.CASCADE, related_name = 'DonatorPraiseComment')
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)