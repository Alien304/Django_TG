from .models import Expansion

def add_expansions(request):
    expansions = Expansion.objects.all()
    return {'expansions': expansions}
