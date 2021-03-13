from django.contrib import admin

# Register your models here.


from .models import Tag, Tag_Type, Arching_Tag, Organization, Quote

admin.site.register(Tag)
admin.site.register(Tag_Type)
admin.site.register(Arching_Tag)

admin.site.register(Organization)
admin.site.register(Quote)