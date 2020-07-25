from django.db import models

class HelpPost(models.Model):
    reciever = models.ForeignKey('mainApp.Receiver', related_name='receiver', on_delete=models.CASCADE, null=False, blank=False, verbose_name="수혈자")
    pub_date = models.DateTimeField(null=False, blank=False, verbose_name="게시일")
    deadLine = models.DateField(null=False, blank=False, verbose_name="마감일")
    finished = models.BooleanField(default=False, null=False, blank=False, verbose_name="마감 여부")
    description = models.TextField(null=False, blank=False, verbose_name="특이사항")

class RecieverComment(models.Model):
    author = models.ForeignKey('mainApp.Receiver', related_name='receiverCommentAuthor', null=False, blank=False, on_delete=models.CASCADE, verbose_name="댓글을 남긴 수혈자")
    pub_date = models.DateTimeField(null=False, blank=False, verbose_name="댓글 작성일")
    body = models.TextField(null=False, blank=False, verbose_name="댓글 내용")

class DonatorComment(models.Model):
    author = models.ForeignKey('mainApp.Donator', related_name='donatorCommentAuthor', on_delete=models.CASCADE, null=False, blank=False, verbose_name="댓글을 남긴 헌혈자")
    pub_date = models.DateTimeField(null=False, blank=False, verbose_name="댓글 작성일")
    body = models.TextField(null=False, blank=False, verbose_name="댓글 내용")