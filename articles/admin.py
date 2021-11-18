from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            stat_dict = form.cleaned_data
            i += int(stat_dict.get('is_main') == True)
        if i == 0:
            raise ValidationError('Необходимо выбрать хотя бы одну категорию')
        elif i > 1:
            raise ValidationError('Необходимо выбрать только одну категорию')
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ArticleTagInline,
    ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

