from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def the_dungeon(request):
    return render(request, 'blog/the_dungeon.html', {})

def the_beach(request):
    return render(request, 'blog/the_beach.html', {})

def the_donut(request):
    return render(request, 'blog/the_donut.html', {})

def the_gordon(request):
    return render(request, 'blog/the_gordon.html', {})

def the_mayor_of_springfield(request):
    return render(request, 'blog/the_mayor_of_springfield.html', {})
    

def about_me(request):
    return render(request, 'blog/about_me.html', {})
    
