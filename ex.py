# Django Shell

from django.db import connection, reset_queries
from inventory.models import Brand

Brand.objects.all().delete()

cursor = connection.cursor()
cursor.execute("INSERT INTO inventory_brand (brand_id, name) VALUES (%s, %s)", ['1', 'nike'])


reset_queries()
Brand.objects.create(brand_id=100, name="nike100")
connection.queries