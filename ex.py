# Django Shell
from inventory.models import Product, ProductInventory, ProductType, Brand

Brand.objects.create(brand_id=1, name="nike")

Product(web_id="1234", slug="nike-shoe-1", name="nike-shoe-1", description="ex2", is_active=True).save()

ProductType.objects.create(name="shoe")

ProductInventory.objects.create(sku="123", upc="123", product_type_id=1, product_id=1, brand_id=1, retail_price="10.00", store_price="10.00", sale_price="10.00", weight="100")