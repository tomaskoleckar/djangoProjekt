from kluby.models import Competition

def competitions(request):
    return {'competitions': Competition.objects.all()}