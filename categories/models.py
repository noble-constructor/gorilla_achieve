from django.db import models


class Category(models.Model):
    """カテゴリクラス.
    name: 名称
    """
    name = models.CharField(max_length=32)
