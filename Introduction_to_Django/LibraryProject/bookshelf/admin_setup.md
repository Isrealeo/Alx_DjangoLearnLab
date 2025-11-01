# Django Admin Setup for Book Model

## Steps Implemented

1. Registered the Book model in `bookshelf/admin.py`.
2. Created a custom admin class `BookAdmin` to:
   - Display title, author, publication_year
   - Enable filtering by publication_year
   - Enable search by title and author
3. Accessed the admin at http://127.0.0.1:8000/admin/
4. Verified that books can be added, edited, deleted, and filtered.
