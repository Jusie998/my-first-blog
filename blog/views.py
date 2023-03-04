from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blogz/post_list.html', {})

def route_two(request):
    return render(request, 'blogz/route2.html', {})
