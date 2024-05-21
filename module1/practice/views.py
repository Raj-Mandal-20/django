from django.http import HttpResponse
from django.shortcuts import render


# Practice For exercise 1 : video 7
# def Home(request):
#     return HttpResponse("<H1> Home Page </h1> <br> <a href='https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'> Django PlayList</a> <br> <a href='https://www.flipkart.com/'> Flipkart</a> <br> <a href='https://www.facebook.com/'> Facebook </a> <br> <a href='https://www.amazon.in/'> amazon</a>  <br> <a href='https://codeforces.com/'> Codeforces</a>")

#Practice For Video no 7

def isPunctuation(item):
    # checked for alphabets
    punctuation = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    for i in range(len(punctuation)):
        if(punctuation[i] == item) :
            return True
        
    return False

def index(request):
    params = {'name' : 'Raj', 'place' : 'India'}
    return render(request, 'index.html', params)
    
def about(request):
    typedData = request.GET.get('typedData', 'default')
    isChecked = request.GET.get('isChecked', 'off')
    
    params = {
        'motivation' : 'Remove Punctuation',
        'before' : typedData,
        'after' : typedData
    }
    
    if(isChecked == 'on') :
        # params['after'] = 'modified'
        removedPunc = ""
        for i in range(len(typedData)):
            if isPunctuation(typedData[i]) == False :
                removedPunc += typedData[i]
        
        params['after'] = removedPunc    
        
    return render(request, 'about.html', params)

def textAnalyze(request):
    return render(request, 'textanalyze.html')