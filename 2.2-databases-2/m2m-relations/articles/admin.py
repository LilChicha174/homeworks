from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        flag = 0
        for form in self.forms:

            if form.cleaned_data.get('DELETE'):
                continue

            if form.cleaned_data.get('is_main'):
                flag += 1

            if flag > 1:
                raise ValidationError('Выберите 1 основной раздел.')

        if flag == 0:
            raise ValidationError('Выберите 1 основной раздел.')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Tag)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name']
