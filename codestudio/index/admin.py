from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Index, Slider, IndexSeo, Location, Feedback


class SliderAdmin(admin.TabularInline):
    model = Slider
    extra = 1
    fields = ['name', 'image', 'alt']


class IndexSeoAdmin(admin.TabularInline):
    model = IndexSeo
    extra = 1
    fields = ['keywords', 'description']


class LocationAdmin(admin.TabularInline):
    model = Location
    extra = 1
    fields = ['latitude', 'longitude']


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows': 6, 'cols': 100})}}
    list_display = ['title', 'get_short_text']
    inlines = [SliderAdmin, IndexSeoAdmin, LocationAdmin]
    search_fields = 'title', 'text'


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'get_short_message')
    readonly_fields = ('name', 'email', 'created', 'message')
    search_fields = 'name', 'email'
