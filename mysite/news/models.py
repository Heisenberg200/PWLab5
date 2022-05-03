from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    content = models.TextField('контент', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True)
    photo = models.ImageField('фото', upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField('опубликовать', default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

   # само строит ссылку
    def get_absolute_url(self):
        # return reverse('view_news', kwargs={'news_id': self.pk})
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,verbose_name='Наименование категории')

    # само строит ссылку
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']