from django.db import models
from achieves.models import Achieve, Status


class User(models.Model):
    """ユーザクラス.
    name: 名前
    image: 画像
    achieves
    """

    name = models.CharField(max_length=32)
    image = models.ImageField()
    achieves = models.ManyToManyField(Achieve, through='UserAchieveRelation')


class UserAchieveRelation(models.Model):
    """実績状態クラス.
    user: ユーザ
    achieve: 実績
    status: 状態
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achieve = models.ForeignKey(Achieve, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
