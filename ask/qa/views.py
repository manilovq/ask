from django.shortcuts import render

from django.http import HttpResponse
def test(request, *args, **kwargs):
    html = "<html><body>test</body></html>"
    return HttpResponse(html)
