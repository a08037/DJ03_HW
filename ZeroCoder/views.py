from django.http import HttpResponse

def data_view(request):
    return HttpResponse("<h1>Страница Data</h1><p>Это контент для страницы Data.</p>")

def test_view(request):
    return HttpResponse("<h1>Страница Test</h1><p>Это контент для страницы Test.</p>")
