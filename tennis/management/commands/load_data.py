from django.core.management.base import BaseCommand
import xlrd

from tennis.models import Match, Tournament


class Command(BaseCommand):
    help = 'load data from tennis-data file'

    def add_arguments(self, parser):
        parser.add_argument('data_file')
        parser.add_argument('sheet_name')

    def handle(self, *args, **options):
        excel_stream = excel_data_stream(options['data_file'],
                                         options['sheet_name'])
        tennis_extractor(excel_stream)


def tennis_extractor(stream):
    context = next(stream)
    header = next(stream)
    for record in stream:
        record = dict(zip(header, record))  # NOTE: not the most efficient
        tournament_fields = dict(
            location=record['Location'],
            name=record['Tournament'],
            series=record['Series'],
            court=record['Court'],
            surface=record['Surface'],
            men_max_nb_set=to_int(record['Best of']),
        )
        tournament, created = Tournament.objects.get_or_create(
            **tournament_fields)

        match_fields = dict(
            tournament=tournament,
            round=record['Round'],
            date=to_date(record['Date'], context.datemode),
            winner=record['Winner'],
            loser=record['Loser'],

            winner_rank=to_int(record['WRank']),
            loser_rank=to_int(record['LRank']),
            winner_points=to_int(record['WPts']),
            loser_points=to_int(record['LPts']),
            w1=to_int(record['W1']),
            w2=to_int(record['W2']),
            w3=to_int(record['W3']),
            w4=to_int(record['W4']),
            w5=to_int(record['W5']),
            l1=to_int(record['L1']),
            l2=to_int(record['L2']),
            l3=to_int(record['L3']),
            l4=to_int(record['L4']),
            l5=to_int(record['L5']),
            comment=record['Comment'],

            B365W=to_float(record.get('B365W', '')),
            B365L=to_float(record.get('B365L', '')),
            BWW=to_float(record.get('BWW', '')),
            BWL=to_float(record.get('BWL', '')),
            CBW=to_float(record.get('CBW', '')),
            CBL=to_float(record.get('CBL', '')),
            EXW=to_float(record.get('EXW', '')),
            EXL=to_float(record.get('EXL', '')),
            LBW=to_float(record.get('LBW', '')),
            LBL=to_float(record.get('LBL', '')),
            GBW=to_float(record.get('GBW', '')),
            GBL=to_float(record.get('GBL', '')),
            IWW=to_float(record.get('IWW', '')),
            IWL=to_float(record.get('IWL', '')),
            PSW=to_float(record.get('PSW', '')),
            PSL=to_float(record.get('PSL', '')),
            SBW=to_float(record.get('SBW', '')),
            SBL=to_float(record.get('SBL', '')),
            SJW=to_float(record.get('SJW', '')),
            SJL=to_float(record.get('SJL', '')),
            UBW=to_float(record.get('UBW', '')),
            UBL=to_float(record.get('UBL', '')),
            MaxW=to_float(record.get('MaxW', '')),
            MaxL=to_float(record.get('MaxL', '')),
            AvgW=to_float(record.get('AvgW', '')),
            AvgL=to_float(record.get('AvgL', '')),
        )
        Match.objects.create(**match_fields)


def excel_data_stream(filename, sheet_name):
    wb = xlrd.open_workbook(filename)
    yield wb
    sheet = wb.sheet_by_name(sheet_name)
    for row_index in range(sheet.nrows):
        yield [cell.value for cell in sheet.row(row_index)]


def to_date(value, date_mode):
    return xlrd.xldate.xldate_as_datetime(value, date_mode)


def to_int(value, default=None):
    try:
        return int(value)
    except ValueError:
        return default


def to_float(value, default=None):
    try:
        return float(value)
    except ValueError:
        return default
