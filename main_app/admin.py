from django.contrib import admin

# Register your models here.
from .models import Dog, Feeding, Toy, Photo

admin.site.register(Dog)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)