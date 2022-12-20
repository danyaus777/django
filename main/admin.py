from django.contrib import admin
from .models import User, DesignForm, Category, AddCommentary, AddImage
from .forms import DFAdminForm

admin.site.register(User)
admin.site.register(Category)


class AddCommentaryInLine(admin.TabularInline):
    model = AddCommentary


class AddImageInLine(admin.TabularInline):
    model = AddImage


class DateRead(admin.ModelAdmin):
    readonly_fields = ('created_date',)


class DFAdmin(admin.ModelAdmin):
    list_display = ('title', 'descript', 'category', 'image', 'user', 'created_date', 'status', 'imagecanc')
    fields = ('title', 'descript', 'category', 'image', 'user', 'status', 'imagecanc')
    readonly_fields = ('created_date',)
    inlines = (AddCommentaryInLine, AddImageInLine)
    list_filter = ('status', 'category')
    form = DFAdminForm


admin.site.register(DesignForm, DFAdmin)
admin.site.register(AddCommentary)
admin.site.register(AddImage)