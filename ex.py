# Django Shell
import datetime
from inventory.models import Product, ProductInventory, ProductType, Brand
from django.db import connection

ProductInventory.objects.all().delete()
Brand.objects.all().delete()
Product.objects.all().delete()
ProductType.objects.all().delete()

Brand.objects.create(brand_id=1, name="nike")
Product(web_id="1234", slug="nike-shoe-1", name="nike-shoe-1", description="ex2", is_active=True).save()
ProductType.objects.create(name="shoe")

datetime_object = datetime.datetime.now()
datetime_object
print(datetime_object)

cursor = connection.cursor()
cursor.execute("INSERT INTO inventory_productinventory(sku,upc,product_type_id,product_id,brand_id,is_active,is_default,retail_price,store_price,sale_price,is_on_sale,is_digital,weight,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",['123','123',1,1,1,True,True,'10.00','10.00','10.00',True,True,'100','2022-08-17 23:47:05.813475','2022-08-17 23:47:05.813475'])
ProductInventory.objects.values()
