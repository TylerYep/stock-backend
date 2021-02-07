from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    del request
    return HttpResponse("Hello, world. You're at the polls index.")
