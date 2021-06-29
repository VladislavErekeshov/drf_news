from django.db import models

# Create your models here.
class News(models.Model):
    date = models.DateField('Дата новости')
    title = models.CharField('Заголовок новости', max_length=50)
    text = models.TextField('Текст новости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'