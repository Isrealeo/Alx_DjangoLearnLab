
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Library
from .models import Book
from django.contrib.auth.views import LoginView, LogoutView 
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



# ✅ Function-Based View: List all books
def list_books(request):
    books = Book.objects.select_related('author').all()  # more efficient with joins
    return render(request, 'relationship_app/list_books.html', {'books': books})

# relationship_app/views.py (continuing same file)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # this matches {{ library }} in the template
# relationship_app/views.py
# relationship_app/views.py


class UserRegisterView(CreateView):
    """Handles new user registration using Django's built-in UserCreationForm."""
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    """Handles user login using Django's built-in LoginView."""
    template_name = 'relationship_app/login.html'


class UserLogoutView(LogoutView):
    """Handles user logout using Django's built-in LogoutView."""
    template_name = 'relationship_app/logout.html'



# relationship_app/views.py
from django.contrib.auth.decorators import user_passes_test, login_required

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    """Accessible only to Admin users."""
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    """Accessible only to Librarian users."""
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    """Accessible only to Member users."""
    return render(request, 'relationship_app/member_view.html')



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book, Author
from .forms import BookForm  # We'll create a simple form

# ----------------------------
# View to list all books
# ----------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ----------------------------
# Add a new book
# ----------------------------
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# ----------------------------
# Edit a book
# ----------------------------
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

# ----------------------------
# Delete a book
# ----------------------------
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # or any page, e.g. 'home'
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

