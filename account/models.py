from django.db import models
from django.contrib.auth.models import AbstractUser

# 기본 User
class RedUser(AbstractUser):
    IDENTIFICATION = (
        ('reciever', '수혈자'),
        ('donator', '헌혈자'),
    )

    # 닉네임
    nickname = models.CharField(max_length = 20, blank = False, null = False, verbose_name = "닉네임")

    # 전화번호
    phone_number = models.CharField(max_length = 15, blank = False, null = False, verbose_name = "전화번호")

    # 혈액형
    bllodType = models.CharField(max_length = 5, blank = False, null = False, verbose_name = "혈액형")

    # 위치
    Location = models.CharField(max_length = 100, blank = False, null =False, verbose_name = "위치")