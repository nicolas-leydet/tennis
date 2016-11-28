from django.contrib import admin

from .models import Tournament, Match


class TourtnamentAdmin(admin.ModelAdmin):
    list_display = ('name',  'location', 'series', 'court', 'surface',
                    'men_max_nb_set')


class MatchAdmin(admin.ModelAdmin):
    list_display = ('get_tournament_name', 'round', 'date', 'winner', 'loser')

    fieldsets = (
        (None, {
            'fields': (('tournament', 'round', 'date'),
                       ('winner', 'loser'))
        }),
        ('ATP status before the match', {
            'fields': (('winner_rank', 'winner_points'),
                       ('loser_rank', 'loser_points'))
        }),
        ('Score', {
            'fields': (('w1', 'l1'), ('w2', 'l2'), ('w3', 'l3'),
                       ('w4', 'l4'), ('w5', 'l5'), 'comment')
        }),
        ('Betting odds', {
            'fields': (('B365W', 'B365L'),
                       ('BWW', 'BWL'),
                       ('CBW', 'CBL'),
                       ('EXW', 'EXL'),
                       ('LBW', 'LBL'),
                       ('GBW', 'GBL'),
                       ('IWW', 'IWL'),
                       ('PSW', 'PSL'),
                       ('SBW', 'SBL'),
                       ('SJW', 'SJL'),
                       ('UBW', 'UBL'),
                       ('MaxW', 'MaxL', 'AvgW', 'AvgL'))
        }),
    )

    def get_tournament_name(self, obj):
        return obj.tournament.name
    get_tournament_name.admin_order_field  = 'tournament__name'
    get_tournament_name.short_description = 'Tournament'


admin.site.register(Tournament, TourtnamentAdmin)
admin.site.register(Match, MatchAdmin)
