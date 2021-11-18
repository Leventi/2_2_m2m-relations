from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    article_tag = models.ManyToManyField(Article, through='ArticleTag')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class ArticleTag(models.Model):
    article = models.ForeignKey('Article', related_name='scopes', on_delete=models.CASCADE, verbose_name='Статьи')
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, verbose_name='Категории')
    is_main = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статей'

