from django import http
from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def index(request):
    context ={
        'AllTheBooks': Book.objects.all()
    }
    return render(request, 'index.html', context)

def createBook(request):
    if request.method == 'POST':
        BookTitle = request.POST['title']
        BookDesc = request.POST['description']
        Book.objects.create(title=BookTitle, desc=BookDesc)
        return redirect('/')

def bookOne(request):
    context ={
        'CSharp': Book.objects.get(id=1),
        'BookAuthors': Book.objects.get(id=1).authors.all(),
        'AllAuthors': Author.objects.all(),
    }
    return render(request, 'bookOne.html', context)

def addAuthorOne(request):
    if request.method == 'POST':
        Author = request.POST['author']
        Book.objects.get(id=1).authors.add(Author)
        return redirect('/bookOne')

def addAuthorTwo(request):
    if request.method == 'POST':
        Author = request.POST['author']
        Book.objects.get(id=2).authors.add(Author)
        return redirect('/bookTwo')

def addAuthorThree(request):
    if request.method == 'POST':
        Author = request.POST['author']
        Book.objects.get(id=3).authors.add(Author)
        return redirect('/bookThree')

def addAuthorFour(request):
    if request.method == 'POST':
        Author = request.POST['author']
        Book.objects.get(id=4).authors.add(Author)
        return redirect('/bookFour')

def addAuthorFive(request):
    if request.method == 'POST':
        Author = request.POST['author']
        Book.objects.get(id=5).authors.add(Author)
        return redirect('/bookFive')

def bookTwo(request):
    context={
        'Java': Book.objects.get(id=2),
        'BookAuthors': Book.objects.get(id=2).authors.all(),
        'AllAuthors': Author.objects.all()
    }
    return render(request, 'bookTwo.html', context)

def bookThree(request):
    context={
        'Python': Book.objects.get(id=3),
        'BookAuthors': Book.objects.get(id=3).authors.all(),
        'AllAuthors': Author.objects.all()
    }
    return render(request, 'bookThree.html', context)

def bookFour(request):
    context={
        'PHP': Book.objects.get(id=4),
        'BookAuthors': Book.objects.get(id=4).authors.all(),
        'AllAuthors': Author.objects.all()
    }
    return render(request, 'bookFour.html', context)

def bookFive(request):
    context={
        'Ruby': Book.objects.get(id=5),
        'BookAuthors': Book.objects.get(id=5).authors.all(),
        'AllAuthors': Author.objects.all()
    }
    return render(request, 'bookFive.html', context)
    
def authors(request):
    context={
        'AllTheAuthors': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def createAuthor(request):
    if request.method == 'POST':
        FirstName = request.POST['first_name']
        LastName = request.POST['last_name']
        Notes = request.POST['notes']
        Author.objects.create(first_name=FirstName, last_name=LastName, notes=Notes)
        return redirect('/authors')

def authorOne(request):
    context={
        'Jane': Author.objects.get(id=1),
        'Books': Author.objects.get(id=1).books.all(),
        'AllTheBooks': Book.objects.all()
    }
    return render(request, 'authorOne.html', context)

def authorTwo(request):
    context={
        'Fyodor': Author.objects.get(id=3),
        'Books': Author.objects.get(id=3).books.all(),
        'AllTheBooks': Book.objects.all()
    }
    return render(request, 'authorTwo.html', context)

def authorThree(request):
    context={
        'William': Author.objects.get(id=4),
        'Books': Author.objects.get(id=4).books.all(),
        'AllTheBooks': Book.objects.all()
    }
    return render(request, 'authorThree.html', context)

def authorFour(request):
    context={
        'Lau': Author.objects.get(id=5),
        'Books': Author.objects.get(id=5).books.all(),
        'AllTheBooks': Book.objects.all()
    }
    return render(request, 'authorFour.html', context)

def addBookOne(request):
    if request.method == 'POST':
        book = request.POST['Books']
        Author.objects.get(id=1).books.add(book)
        return redirect('/authorOne')

def addBookTwo(request):
    if request.method == 'POST':
        book = request.POST['Books']
        Author.objects.get(id=3).books.add(book)
        return redirect('/authorTwo')

def addBookThree(request):
    if request.method == 'POST':
        book = request.POST['Books']
        Author.objects.get(id=4).books.add(book)
        return redirect('/authorThree')

def addBookFour(request):
    if request.method == 'POST':
        book = request.POST['Books']
        Author.objects.get(id=5).books.add(book)
        return redirect('/authorFour')