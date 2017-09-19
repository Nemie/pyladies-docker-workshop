from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, pyLadies! I'm a Django app!")
