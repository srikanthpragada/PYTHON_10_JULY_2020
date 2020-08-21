from django.shortcuts import render
from django.http import HttpResponse

quotes = ['Winners never quit, Quitters never win',
          'If you are not failing, you are not growing',
          'Be the change you want to see']
pos = 0


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def get_quote(request):
    global pos
    if pos == len(quotes) - 1:
        pos = 0
    else:
        pos += 1

    return HttpResponse(quotes[pos])
