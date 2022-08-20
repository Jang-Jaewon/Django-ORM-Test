# Django Shell
import datetime
from inventory.models import Product, ProductInventory, ProductType, Brand, Category
from django.db import connection, reset_queries

ProductInventory.objects.all().delete()
Brand.objects.all().delete()
Product.objects.all().delete()
ProductType.objects.all().delete()
Category.objects.all().delete()

reset_queries() \

x = Product(web_id="1234", slug="ex1", name="ex3", description="ex3", is_active=True)
x.save()
y = Category(name="Flip-Flops", slug="fliplops", is_active=True)
y.save()
connection.queries

reset_queries()
x.category.add(y)
connection.queries
"""
[{'sql': 'BEGIN', 'time': '0.000'}, 
{'sql': 'INSERT OR IGNORE INTO "inventory_product_category" ("product_id", "category_id") SELECT 6, 3', 'time': '0.001'}]
"""


# SQL로 ManyToManyField INSET
cusror = connection.cursor()
cusror.execute("INSERT INTO inventory_product (web_id,slug,name,description,is_active,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s)", ['12345', 'ex4', 'ex4', 'ex4', True, '2022-05-31 16:08:08.725532', '2022-05-31 16:08:08.725532'])
cusror.execute("INSERT INTO inventory_category (name,slug,is_active) VALUES (%s,%s,%s)", ['Flip-Flops', 'flipflops', True])
Product.objects.first().id # 7
Category.objects.first().id # 4
cusror.execute("INSERT INTO inventory_product_category (product_id, category_id) VALUES (%s,%s)", [7, 4])

p = Product.objects.first()
p.category.all()
