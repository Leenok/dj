from django.contrib import admin
from app1.models import pzzle, Producer, size


class myPuzzle(admin.ModelAdmin):
    list_display = ["name", "detail", "style", "material", "age", "price", "count"]

admin.site.register(pzzle, myPuzzle)
admin.site.register(Producer)
admin.site.register(size)