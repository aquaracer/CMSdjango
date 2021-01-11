from django.contrib import admin
from django.utils.html import format_html
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import *


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 1


@admin.register(IndexPage)
class IndexPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

    inlines = [PhotoInline, ParagraphInline]


class SuboptionInline(NestedStackedInline):
    model = Suboption
    extra = 1
    fk_name = 'option'


class OptionInline(NestedStackedInline):
    model = Option
    extra = 1
    min_num = 1
    max_num = 3
    fk_name = 'product'
    inlines = [SuboptionInline]


@admin.register(Product)
class ProductAdmin(NestedModelAdmin):
    model = Product
    inlines = [OptionInline, ]
    ordering = ('created',)

    def change_button(self, obj):
        return format_html('<a class="button" href="/admin/cms/product/{}/change/">Изменить</a>',
                           obj.id)

    change_button.short_description = ''

    def delete_button(self, obj):
        return format_html('<a class="button" href="/admin/cms/product/{}/delete/">Удалить</a>', obj.id)

    delete_button.short_description = ''

    list_display = ('__str__', 'change_button', 'delete_button')
