from django.db import models
from .utils import Choices


SERIES_CHOICES = Choices(
    ('ATP250', 'ATP250'),
    ('ATP500', 'ATP500'),
    ('GRAND_SLAM', 'Grand Slam'),
    ('MASTERS_1000', 'Masters 1000'),
    ('MASTERS_CUP', 'Masters Cup'),
)

COURT_CHOICES = Choices(
    ('INDOOR', 'Indoor'),
    ('OUTDOOR', 'Outdoor'),
)

SURFACE_CHOICES = Choices(
    ('CARPET', 'Carpet'),
    ('CLAY', 'Clay'),
    ('GRASS', 'Grass'),
    ('HARD', 'Hard'),
)


class Tournament(models.Model):
    SERIES = SERIES_CHOICES.get_const()
    COURT = COURT_CHOICES.get_const()
    SURFACE = SURFACE_CHOICES.get_const()

    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    series = models.CharField(
        max_length=20,
        choices=SERIES_CHOICES.get_choices(),
        default=SERIES.ATP250,
    )
    court = models.CharField(
        max_length=20,
        choices=COURT_CHOICES.get_choices(),
    )
    surface = models.CharField(
        max_length=20,
        choices=SURFACE_CHOICES.get_choices(),
    )
    men_max_nb_set = models.PositiveIntegerField()

    def __str__(self):
        return '{} - {}'.format(self.name, self.location)


ROUND_CHOICES = Choices(
    ('ROUND_ROBIN', 'Round Robin'),
    ('FIRST_ROUND', '1st Round'),
    ('SECOND_ROUND', '2nd Round'),
    ('THIRD_ROUND', '3rd Round'),
    ('FOURTH_ROUND', '4th Round'),
    ('QUARTER', 'Quarterfinals'),
    ('SEMI', 'Semifinals'),
    ('FINAL', 'The Final'),
)

COMMENT_CHOICES = Choices(
    ('COMPLETED', 'Completed'),
    ('RETIRED', 'Retired'),
    ('WALKOVER', 'Walkover'),
)


class Match(models.Model):
    ROUND = ROUND_CHOICES.get_const()
    COMMENT = COMMENT_CHOICES.get_const()

    tournament = models.ForeignKey(Tournament)
    round = models.CharField(
        max_length=20,
        choices=ROUND_CHOICES.get_choices(),
    )
    date = models.DateField()
    winner = models.CharField(max_length=50)
    loser = models.CharField(max_length=50)

    winner_rank = models.PositiveIntegerField(null=True)
    loser_rank = models.PositiveIntegerField(null=True)
    winner_points = models.PositiveIntegerField(null=True)
    loser_points = models.PositiveIntegerField(null=True)
    w1 = models.PositiveIntegerField(null=True)
    w2 = models.PositiveIntegerField(null=True)
    w3 = models.PositiveIntegerField(null=True)
    w4 = models.PositiveIntegerField(null=True)
    w5 = models.PositiveIntegerField(null=True)
    l1 = models.PositiveIntegerField(null=True)
    l2 = models.PositiveIntegerField(null=True)
    l3 = models.PositiveIntegerField(null=True)
    l4 = models.PositiveIntegerField(null=True)
    l5 = models.PositiveIntegerField(null=True)
    comment = models.CharField(
        max_length=20,
        choices=COMMENT_CHOICES.get_choices(),
    )

    B365W = models.FloatField(null=True)
    B365L = models.FloatField(null=True)
    BWW = models.FloatField(null=True)
    BWL = models.FloatField(null=True)
    CBW = models.FloatField(null=True)
    CBL = models.FloatField(null=True)
    EXW = models.FloatField(null=True)
    EXL = models.FloatField(null=True)
    LBW = models.FloatField(null=True)
    LBL = models.FloatField(null=True)
    GBW = models.FloatField(null=True)
    GBL = models.FloatField(null=True)
    IWW = models.FloatField(null=True)
    IWL = models.FloatField(null=True)
    PSW = models.FloatField(null=True)
    PSL = models.FloatField(null=True)
    SBW = models.FloatField(null=True)
    SBL = models.FloatField(null=True)
    SJW = models.FloatField(null=True)
    SJL = models.FloatField(null=True)
    UBW = models.FloatField(null=True)
    UBL = models.FloatField(null=True)
    MaxW = models.FloatField(null=True)
    MaxL = models.FloatField(null=True)
    AvgW = models.FloatField(null=True)
    AvgL = models.FloatField(null=True)
