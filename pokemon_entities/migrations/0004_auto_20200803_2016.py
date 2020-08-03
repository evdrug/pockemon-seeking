# Generated by Django 2.2.3 on 2020-08-03 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_pokemonentity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemon',
            options={'verbose_name': 'Покемон', 'verbose_name_plural': 'Покемоны'},
        ),
        migrations.AlterModelOptions(
            name='pokemonentity',
            options={'verbose_name': 'Описание покемона', 'verbose_name_plural': 'Описание покемонов'},
        ),
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolution', to='pokemon_entities.Pokemon', verbose_name='из кого эволюционирует'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(default=None, max_length=200, verbose_name='Имя на английском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(default=None, max_length=200, verbose_name='Имя на японском'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(default=None, upload_to='', verbose_name='Картинка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(verbose_name='Время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(blank=True, null=True, verbose_name='Защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(verbose_name='Время исчезновения'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, null=True, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, null=True, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon', verbose_name='Покемон'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, null=True, verbose_name='Выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сила'),
        ),
    ]