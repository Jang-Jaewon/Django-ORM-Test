# Django Shell
from inventory.models import Brand
import cProfile
from django.db import connection, reset_queries


Brand.objects.all().delete()

def using_multiple_inserts():
    for n in range(10000):
        Brand.objects.create(brand_id=n, name=n)

p = cProfile.Profile()
p.runcall(using_multiple_inserts)
p.print_stats(sort="tottime")
# 2420037 function calls (2380037 primitive calls) in 4.064 seconds

using_multiple_inserts() # 함수 호출
connection.queries # SQL 보기(10000개의 Qeury)


Brand.objects.all().delete()

def using_bulk_create():
    Brand.objects.bulk_create([Brand(brand_id=n, name=n) for n in range(10000)])

p = cProfile.Profile()
p.runcall(using_bulk_create)
p.print_stats(sort="tottime")
#  844254 function calls (834186 primitive calls) in 0.223 seconds

reset_queries()
using_bulk_create() # 함수 호출
connection.queries # SQL 보기(1개의 Qeury)
