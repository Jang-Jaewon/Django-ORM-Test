# Django Shell
import datetime
from inventory.models import Product, ProductInventory, ProductType, Brand, Category
from django.db import connection

ProductInventory.objects.all().delete()
Brand.objects.all().delete()
Product.objects.all().delete()
ProductType.objects.all().delete()

x = Product(web_id="1234", slug="ex1", name="ex3", description="ex3", is_active=True)
x.save()
y = Category(name="Flip-Flops", slug="fliplops", is_active=True)
y.save()

x = Product(web_id="12346", slug="ex10", name="ex10", description="ex10", is_active=True)
x.save()

x.category.add(y)

x = Product(web_id="123467", slug="ex100", name="ex100", description="ex100", is_active=True)
x.save()

x = Product.objects.get(id=4)
y = Category.objects.get(id=1)

x.category.add(y)
x.category.all()


y = Category(name="cate2", slug="cate2", is_active=True)
y.save()
x.category.add(Category.objects.get(id=2))
x.category.all()

x = Product(web_id="1010", slug="ex7", name="ex7", description="ex7", is_active=True)
x.save()
x.category.all()

y = Category.objects.all()
x.category.add(*y)
x.category.all()