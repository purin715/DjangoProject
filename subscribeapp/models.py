from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscrption', null=False)

    class Meta:
        # 외부정보를 설정해준다.
        # 메타데이터 : 필드가 아닌 모든 데이터.
        unique_together = ['user', 'project'] # 연결 쌍이 하나만 존재할 수 있도록.