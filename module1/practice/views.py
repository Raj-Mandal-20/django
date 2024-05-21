from django.http import HttpResponse
from django.shortcuts import render


# Practice For exercise 1 : video 7
# def Home(request):
#     return HttpResponse("<H1> Home Page </h1> <br> <a href='https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'> Django PlayList</a> <br> <a href='https://www.flipkart.com/'> Flipkart</a> <br> <a href='https://www.facebook.com/'> Facebook </a> <br> <a href='https://www.amazon.in/'> amazon</a>  <br> <a href='https://codeforces.com/'> Codeforces</a>")

#Practice For Video no 7
def index(request):
    
    return render(request, 'index.html')
    

def about(request):
    return HttpResponse('''
        <h1> About </h1> <br>
        <a href="/"> Home </a>
                        ''')

def menu(request):
    return HttpResponse('''
        <h1> Menu </h1> <br>
        <a href="/"> Home </a>
                        ''')

def settings(requsest):
    return HttpResponse('''
        <h1> Settings </h1> <br>
        <a href="/"> Home </a>
                        ''')