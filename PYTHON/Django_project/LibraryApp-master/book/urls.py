from django.urls import path
from . import views
from libraryapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

#DataFlair Django Tutorials
urlpatterns = [
	path('', views.index, name = 'index'),
	path('upload/', views.upload, name = 'upload-book'),
	path('update/<int:book_id>', views.update_book),
	path('delete/<int:book_id>', views.delete_book)
]

#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)


'''x-html has doctype manadatory while html doesn't require you to declare doctype
xmlns type is mandatory in html
html, head, body and title is mandatory
must be properly nested
must be properly closed
must be used in lowercase

'''