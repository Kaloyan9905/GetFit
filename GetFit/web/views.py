from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    def get(self, request):
        return render(request, 'start-page.html')


def main_page(request):
    context = {}
    return render(request, 'main.html', context)
