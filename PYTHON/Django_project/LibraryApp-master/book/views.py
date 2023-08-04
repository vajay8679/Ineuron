from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

#DataFlair
def index(request):
	shelf = Book.objects.all()
	return render(request, 'book/library.html', {'shelf': shelf})

def upload(request):
	upload = BookCreate()
	if request.method == 'POST':
		upload = BookCreate(request.POST, request.FILES)
		if upload.is_valid():
			upload.save()
			return redirect('index')
		else:
			return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
	else:
		return render(request, 'book/upload_form.html', {'upload_form':upload})

def update_book(request, book_id):
	book_id = int(book_id)
	try:
		book_sel = Book.objects.get(id = book_id)
	except Book.DoesNotExist:
		return redirect('index')
	book_form = BookCreate(request.POST or None, instance = book_sel)
	if book_form.is_valid():
		book_form.save()
		return redirect('index')
	return render(request, 'book/upload_form.html', {'upload_form':book_form})

def delete_book(request, book_id):
	book_id = int(book_id)
	try:
		book_sel = Book.objects.get(id = book_id)
	except Book.DoesNotExist:
		return redirect('index')
	book_sel.delete()
	return redirect('index')



















# def details(request, book_id):
# 	book_id = int(book_id)
# 	try:
# 		book_sel = Book.objects.get(id = book_id)
# 	except Book.DoesNotExist:
# 		return redirect('index')
# 	url = book_sel.picture.url
# 	return render(request, 'book/details.html', {'book':book_sel, 'url':url})
