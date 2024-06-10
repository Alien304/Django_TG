from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Card, Expansion

def my_view(request):
    expansions = Expansion.objects.all()
    return render(request, 'my_template.html', {'expansions': expansions})

def cards_by_expansion(request, expansion_name):
    expansion = get_object_or_404(Expansion, expansion_name=expansion_name)
    cards = Card.objects.filter(expansion_name=expansion)
    return render(request, 'cards/cards_by_expansion.html', {'expansions': expansion, 'cards': cards})

def cards_by_expansion_ajax(request):
    expansion_name = request.GET.get('expansion_name')
    expansion = get_object_or_404(Expansion, expansion_name=expansion_name)
    cards = Card.objects.filter(expansion_name=expansion)
    return render(request, 'cards/cards_list.html', {'expansion': expansion, 'cards': cards, 'user': request.user})

def update_card_ownership(request):
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        is_owned = request.POST.get('is_owned') == 'true'
        card = get_object_or_404(Card, id=card_id)
        if is_owned:
            card.owned_by_users.add(request.user)
        else:
            card.owned_by_users.remove(request.user)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})