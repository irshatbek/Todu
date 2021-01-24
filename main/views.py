from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import BookShop


def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def fizz_buzz(request):
    def num_x(a):
    
        if a % 3 == 0 and a % 5 == 0:
            return HttpResponse("FizzBuzz")

        elif a % 3 == 0:
            return HttpResponse("Fizz")

        elif a % 5 == 0:
            return HttpResponse("Buzz")
        
        else:
            return HttpResponse(a)
    x = num_x(1)
    return HttpResponse(x)

def second(request):
    return HttpResponse("test 2 page 222")

def info_one(request):
    return render(request, "info.html")

def info_change(request):
    return render(request, "info_change.html")

def info_dell(request):
    return render(request, "info_dell.html")

def bookshop(request):
    return render(request, "bookshop.html")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo (text=text)
    todo.save()
    return redirect(test)

def add_title(request):
    form = request.POST
    text = form["title_text"]
    todo = ToDo (text=text)
    todo.save()
    return redirect(test)

def bs_f(request):
    book_shop = BookShop.objects.all()
    return render(request, "bs.html", {"book_shop": book_shop})
