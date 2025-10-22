from django.db import models


class Index(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок', help_text='введите заголовок главной страницы')
    text = models.TextField(verbose_name='текст на главной', help_text='введите текст статьи на главной странице')

    class Meta:
        verbose_name = 'контент на главную страницу'
        verbose_name_plural = 'главная'

    def __str__(self):
        return self.title

    # выводим первые 120 символов текста главной, для компактности админки
    def get_short_text(self):
        if len(self.text) < 120:
            return self.text
        return self.text[:120] + '...'

    get_short_text.short_description = 'Краткое содержание текста'


class Slider(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя изображения', help_text='имя слайда до 200 знаков')
    image = models.ImageField(upload_to='slider/', verbose_name='изображение',
                              help_text='слайд в формате .jpg или .png')
    alt = models.CharField(max_length=200, verbose_name='alt-текст', help_text='alt-текст к слайду')
    fk_index = models.ForeignKey(Index, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'слайдер'
        verbose_name_plural = 'слайдер'

    def __str__(self):
        return self.name


class IndexSeo(models.Model):
    keywords = models.CharField(max_length=250, verbose_name='ключевые слова (keywords)',
                                help_text='SEO ключевые слова через запятую, до 250 знаков')
    description = models.CharField(max_length=200, verbose_name='описание (description)',
                                   help_text='SEO описание до 200 знаков')
    fk_index = models.ForeignKey(Index, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'seo-оптимизатор'
        verbose_name_plural = 'seo-оптимизатор (Index Page)'

    def __str__(self):
        return self.description


class Location(models.Model):
    latitude = models.FloatField(null=True, blank=True, verbose_name='широта',
                                 help_text='введите широту в формате 00.00')
    longitude = models.FloatField(null=True, blank=True, verbose_name='долгота',
                                  help_text='введите долготу в формате 00.00')
    fk_index = models.ForeignKey(Index, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'местоположение'

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя отправителя')
    email = models.EmailField(verbose_name='e-mail отправителя')
    message = models.TextField(verbose_name='сообщение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='время отправки')

    class Meta:
        verbose_name = 'сообщение пользователя'
        verbose_name_plural = 'обратная связь'

    def __str__(self):
        return self.name

    # выводим первые 100 символов сообщения, для компактного вида
    def get_short_message(self):
        if len(self.message) < 100:
            return self.message
        return self.message[:100] + '...'

    get_short_message.short_description = 'Краткое содержание текста'
