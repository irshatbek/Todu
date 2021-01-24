from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import BookShop


def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo (text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)




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



def add_book(request):

    form = request.POST
    text_Tit = form["title_text"]
    text_Sub = form["subtitle_text"]
    text_Des = form["description_text"]
    text_Pri = form["price_text"]
    text_Gen = form["genre_text"]
    text_Auth = form["author_text"]
    text_Year = form["year"]
    book_shop = BookShop(text_Title=text_Tit, text_Subtitle=text_Sub, text_Description=text_Des, text_Price=text_Pri, text_Genre=text_Gen, text_Author=text_Auth, text_Year=text_Year)
    book_shop.save()
    return redirect(bs)

def bs(request):
    book_shop = BookShop.objects.all()
    return render(request, "bs.html", {"book_shop": book_shop})

def delete_book(request, id):
    book = BookShop.objects.get(id=id)
    book.delete()
    return redirect(bs)

def mark_book(request, id):
    book = BookShop.objects.get(id=id)
    book.is_favorite = True
    book.save()
    return redirect(bs)

def unmark_book(request, id):
    book = BookShop.objects.get(id=id)
    book.is_favorite = False
    book.save()
    return redirect(bs)

def detail_book(request, id):
    return render(request, "bookshop.html")
