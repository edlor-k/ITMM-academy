from django.contrib import admin
from .models import Token, Profile

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')
    search_fields = ('user__username',)
    list_editable = ('amount',)
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_url')
    search_fields = ('user__username',)