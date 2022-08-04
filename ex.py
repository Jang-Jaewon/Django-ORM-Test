# pip install pygments sqlparse

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

from inventory import Brand

Brand.objects.all().delete()
Brand.objects.create(brand_id=1, name="nike")

x = Brand.objects.filter(brand_id=1)
sqlformatted = format(str(x.query), reindent=True)
print(highlight(sqlformatted, PostgresLexer(), TerminalFormatter()))
