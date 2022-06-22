from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from .forms import *
from user.models import Books
# Create your views here.

#Homepage
def home(request):
    if(request.user.is_authenticated):
        return redirect('view_book/')
    else:
        return render(request,'index.html')

#Function for showing all books in the database
def allbook(request):
    context = {'books' : Books.objects.all()}
    return render(request,'home.html', context)


#Function for login the user/admin
def login_view(request):
    if (request.user.is_authenticated):
        return redirect('/')
    return render(request, 'login.html')


#Function for register the user/admin
def signup_view(request):
    if (request.user.is_authenticated):
        return redirect('/')
    return render(request , 'signup.html')


#Function for Logout
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def add_book(request):
    context = {'form': SaveBook}
    try:
        if request.method == 'POST':
            form = SaveBook(request.POST)
            isbn =  request.POST.get('isbn')
            title =  request.POST.get('title')
            description =  request.POST.get('description')
            author =  request.POST.get('author')
            publisher =  request.POST.get('publisher')
            status =  request.POST.get('status')
            user = request.user

            if form.is_valid():
                Books.objects.create(
                    user = user , title = title, isbn = isbn,
                    description = description, author = author,
                    publisher = publisher, status = status
                )
            else:
                return redirect('/add_book/')

    except Exception as e:
        print(e)
    return render(request, 'book.html', context)

@login_required(login_url='/login/')
def view_book(request):
    context = {}
    try:
        book_objs = Books.objects.filter(user = request.user)
        context['book_objs'] =  book_objs
    except Exception as e: 
        print(e)
    print(context)
    return render(request , 'view_book.html' ,context)

@login_required(login_url='/login/')
def update(request, id):
    context = {}
    try:
        
        book_obj = Books.objects.get(id = id)
        if book_obj.user != request.user:
            return redirect('/')
        print(book_obj.isbn)
        initial_dict = {
            'status': book_obj.status,
            "title" : book_obj.title,
            "isbn" : book_obj.isbn,
            "description" : book_obj.description,
            "author" : book_obj.author,
            "publisher" : book_obj.publisher
        }
        form = SaveBook(initial = initial_dict)

        if request.method == 'POST':
            form = SaveBook(request.POST)
            
            title = request.POST.get('title')
            description = request.POST.get('description')
            status = request.POST.get('status')
            publisher = request.POST.get('publisher')
            author = request.POST.get('author')
            user = request.user
            
            if form.is_valid():
            
                book_obj = Books.objects.update(
                    user = user , title = title, 
                    description = description, status = status,
                    publisher = publisher, author = author
                )
        
        context['book_obj'] = book_obj
        context['form'] = form
    except Exception as e :
        print(e)

    return render(request , 'update.html', context)

def delete(request, id):
    try:
        book_obj = Books.objects.get(id = id)
        
        if book_obj.user == request.user:
            book_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/view_book/')