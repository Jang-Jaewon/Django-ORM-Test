# Django Shell
import datetime
from inventory.models import Product, ProductInventory, ProductType, Brand, Category, Stock
from django.db import connection, reset_queries

ProductInventory.objects.all().delete()
Brand.objects.all().delete()
Product.objects.all().delete()
ProductType.objects.all().delete()
Category.objects.all().delete()

Product.objects.create(web_id="123", slug="ex1", name="ex1", description="ex10000", is_active=True)
Brand.objects.create(brand_id="1", name="ex1")
ProductType.objects.create(name="shoe")

ProductInventory.objects.create(sku="123", upc="123", product_type_id=1, product_id=2, brand_id=1, retail_price="10.00", store_price="10.00", sale_price="10.00", weight="100")

Stock.objects.create(product_inventory_id=1, units=100)
