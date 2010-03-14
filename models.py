import csv

from django.utils.translation import ugettext as _
from django.db import models

from cms.models import CMSPlugin

class CsvCell:
    def __init__(self, content, row, order):
        self.content = content
        self.row = row
        self.odrer = order

class CsvRow:
    def __init__(self, number, columns):
        self.odd = number % 2 != 0
        self.cells = [CsvCell(c, self, ic) for ic,c in enumerate(columns)]

# Derived from CMSPlugin => doesn't exist outside of a page
class CsvTablePlugin(CMSPlugin):
    caption = models.CharField(_('Caption'), max_length=200)
    columns = models.CharField(_('Column layout'), max_length=200,
        help_text=_(
            'Describe the column width and alignment in a comma separated list.\n' +
            'Value: 5>,3,10<  means: '
            'column 1 is 5 units wide and right aligned, ' +
            'column 2 is 3 units wide and centered, ' +
            'column 3 is 10 units wide and left aligned.'
            ))
    csv_data = models.TextField(_('CSV Data'))
    # width = models.IntegerField(_('Table width (%)'), choices=...)
    # border_css = models.CharField(_('Table style'), choices=..., max_length=20)
    # layout_css = models.CharField(_('Table placement'), choices=..., max_length=20)

    def __unicode__(self):
        return u'%s' % (self.caption)

    # TODO: cache rows?
    @property
    def rows(self):
        rows = []
        # XXX: Assume data is in unicode!
        csvRows = csv.reader(self.csv_data.encode("utf8").split("\n"))
        for ir,row in enumerate(csvRows):
            rows.append(CsvRow(ir, [c.decode("utf8") for c in row]))

        return rows
