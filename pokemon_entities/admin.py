from django.contrib import admin

from pokemon_entities.models import Pokemon, PokemonEntity


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass
    # class Meta:
    #     verbose_name = 'Покемон'
    #     verbose_name_plural = 'Покемоны'

@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ('pokemon', 'health', 'strength', 'defence', 'stamina' )
