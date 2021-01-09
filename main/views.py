from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("Hello world!")

def test(request):
    return render(request, "test.html")

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
