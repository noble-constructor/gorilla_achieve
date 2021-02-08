from django.db import models
from categories.models import Category


class Status(models.Model):
    """実績ステータスクラス.
    name: 表示名
    """
    name = models.CharField(max_length=16)


class Achieve(models.Model):
    """実績クラス.
    title: タイトル
    content: 詳細
    categories: カテゴリ
    users: 対象
    """
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=256)
    categories = models.ManyToManyField(Category)



