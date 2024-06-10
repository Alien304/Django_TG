from django.contrib import admin
from .models import Card, Expansion


# Unregister the models if they are already registered
try:
    admin.site.unregister(Card)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(Expansion)
except admin.sites.NotRegistered:
    pass

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_name', 'expansion_name', 'card_number', 'display_owned_by_users')
    search_fields = ['card_name', 'expansion_name__expansion_name']
    
    def display_owned_by_users(self, obj):
        return ", ".join([user.username for user in obj.owned_by_users.all()])
    display_owned_by_users.short_description = 'Owned By'

class ExpansionAdmin(admin.ModelAdmin):
    list_display = ['expansion_name', 'expansion_amount']
    search_fields = ['expansion_name']

admin.site.register(Card, CardAdmin)
admin.site.register(Expansion, ExpansionAdmin)