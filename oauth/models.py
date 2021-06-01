from django.db import models


class SocialUser(models.Model):
    user = models.ForeignKey(
        'cert.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='회원id',
        related_name='socialuser'
    )
    social_user_id = models.CharField('소셜서버에 등록된 회원번호', max_length=100, unique=True, null=False)
    PLATFORM_CHOICES = [('kakao', '카카오'), ('naver', '네이버')]
    social_type = models.CharField(max_length=10, choices=PLATFORM_CHOICES, null=False)
    
    class Meta:
        unique_together = ['social_user_id', 'social_type', 'user']
        db_table = 'socialuser'
        verbose_name = '소셜유저 정보'
