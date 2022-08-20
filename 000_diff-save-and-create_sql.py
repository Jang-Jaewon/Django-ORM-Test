# Django Shell

from inventory.models import Brand, Category
from django.db import connection, reset_queries

Brand.objects.all().delete()

Brand.objects.create(brand_id=1, name="Nike")

Brand(brand_id=1000, name="Nike2").save()

Category.objects.all().delete()

Category.objects.create(name="Trainers", slug="trainers", is_active=True)

Category(id=3, name="Trainers100", slug="trainers2", is_active=True).save()


reset_queries()

Brand.objects.create(brand_id=1, name="Nike")
connection.queries
reset_queries()

Brand(brand_id=1000, name="Nike2").save()
connection.queries
reset_queries()

Brand(brand_id=1000, name="Nike1000").save()
connection.queries
reset_queries() 
