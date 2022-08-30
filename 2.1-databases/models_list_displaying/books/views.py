from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Book


def books_view(request, arg_date=None):
    obj_books = Book.objects.all()
    if not arg_date:
        template = 'books/books_list.html'
        context = {'books': list(obj_books)}
    else:
        page = None
        previous_page_val = None
        next_page_val = None
        obj = sorted(obj_books, key=lambda x: x.pub_date)
        paginator = Paginator(obj, 1)
        template = 'books/pgi.html'
        for dt in obj:
            cur_date = dt.pub_date.strftime('%Y-%m-%d')
            if cur_date == arg_date:
                idx = list(obj).index(dt)
                page = paginator.get_page(idx + 1)
                if idx != len(obj) - 1:
                    next_page_val = obj[idx + 1].pub_date.strftime('%Y-%m-%d')
                if idx != 0:
                    previous_page_val = obj[idx - 1].pub_date.strftime(
                        '%Y-%m-%d')
        context = {'page': page, 'previous_page_val': previous_page_val,
                   'next_page_val': next_page_val}
    return render(request, template, context)
