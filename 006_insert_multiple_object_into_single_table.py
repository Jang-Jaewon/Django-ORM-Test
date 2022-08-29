# Django Shell
from inventory.models import Product, ProductInventory, ProductType, Brand, Category, Stock

Brand.objects.all().delete()

# bulk_create`
x = Brand.objects.bulk_create(
    [
        Brand(brand_id=1, name='ex1'),
        Brand(brand_id=2, name='ex2'),
        Brand(brand_id=3, name='ex3'),

    ]
)
Brand.objects.all()


# Unpack
datas = [
    {'brand_id': 4, 'name': 'ex4'},
    {'brand_id': 5, 'name': 'ex5'},
    {'brand_id': 6, 'name': 'ex6'},
]
Brand.objects.bulk_create([Brand(**data) for data in datas])
Brand.objects.all()