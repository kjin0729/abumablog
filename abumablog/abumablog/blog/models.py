from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField('タイトル', max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('タイトル', max_length=32)
    thumbnail = models.ImageField('サムネイル')
    text = models.TextField('本文')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    create_at = models.DateTimeField('作成日', default=timezone.now)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title


class PostQuerySet(models.QuerySet):
    def pubulished(self):
        return self.filter(create_at__lte=timezone.now())


class Comment(models.Model):
    name = models.CharField('名前', max_length=255, default='名無し')
    text = models.TextField('本文')
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='対象投稿')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    email = models.EmailField('メールアドレス', blank=True, help_text='入力しておくと、返信があった際に通知します。コメント欄には表示されません。')

    def __str__(self):
        return self.text[:20]


class Reply(models.Model):
    name = models.CharField('名前', max_length=255, default='名無し')
    text = models.TextField('本文')
    target = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='対象コメント')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:20]
