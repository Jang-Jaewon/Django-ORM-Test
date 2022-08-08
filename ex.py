# Django Shell

from inventory.models import Brand, Category

Brand.objects.all().delete()

Brand.objects.create(brand_id=1, name="Nike")

Brand(brand_id=1, name="Nike2").save()

Category.objects.all().delete()

Category.objects.create(name="Trainers", slug="trainers", is_active=True)

Category(id=3, name="Trainers100", slug="trainers2", is_active=True).save()