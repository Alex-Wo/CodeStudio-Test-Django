from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок продукта',
                             help_text='заголовок продукта до 200 знаков')
    image = models.ImageField(upload_to='product/', verbose_name='фото продукта',
                              help_text='фото продукта в формате .jpg или .png')
    alt = models.CharField(max_length=200, null=True, verbose_name='alt-текст фото',
                           help_text='alt-текст к фото продукта')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.title


class TextList(models.Model):
    title = models.CharField(max_length=250, verbose_name='заголовок списка',
                             help_text='заголовок списка до 250 знаков')
    fk_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'список текста'
        verbose_name_plural = 'списки текста'

    def __str__(self):
        return self.title


class Point(models.Model):
    text = models.CharField(max_length=250, verbose_name='пункт списка', help_text='текст пункта до 250 знаков')
    fk_textlist = models.ForeignKey(TextList, related_name='points', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'пункт списка'
        verbose_name_plural = 'пункты списка'

    def __str__(self):
        return self.text


class ProductSeo(models.Model):
    keywords = models.CharField(max_length=250, verbose_name='ключевые слова (keywords)',
                                help_text='SEO ключевые слова через запятую, до 250 знаков')
    description = models.CharField(max_length=200, verbose_name='описание (description)',
                                   help_text='SEO описание до 200 знаков')
    fk_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'seo-оптимизатор'
        verbose_name_plural = 'seo-оптимизатор (Product Page)'

    def __str__(self):
        return self.description
