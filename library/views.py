from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'library_home.html')

def book_page(request):
    return render(request,'library_book.html')

def book_detail_page(request,book_num):
    context = {
        'book_num':book_num,
    }
    return render(request,'library_book_detail.html',context)