from django.db import models


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Имя', max_length=200)
    title_en = models.CharField(verbose_name='Имя на английском',
                                max_length=200)
    title_jp = models.CharField(verbose_name='Имя на японском', max_length=200)
    image = models.ImageField(verbose_name='Картинка')
    description = models.TextField(verbose_name='Описание', null=True,
                                   blank=True)
    previous_evolution = models.ForeignKey("self",
                                           verbose_name='из кого эволюционирует',
                                           on_delete=models.CASCADE,
                                           related_name='next_evolution',
                                           null=True,
                                           blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон',
                                on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Время появления')
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения')
    level = models.IntegerField(verbose_name='Уровень', blank=True, null=True)
    health = models.IntegerField(verbose_name='Здоровье', blank=True,
                                 null=True)
    strength = models.IntegerField(verbose_name='Сила', blank=True, null=True)
    defence = models.IntegerField(verbose_name='Защита', blank=True, null=True)
    stamina = models.IntegerField(verbose_name='Выносливость', blank=True,
                                  null=True)

    def __str__(self):
        return self.pokemon.title

    class Meta:
        verbose_name = 'Описание покемона'
        verbose_name_plural = 'Описание покемонов'
