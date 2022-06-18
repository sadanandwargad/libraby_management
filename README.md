# libraby_management
git link - https://github.com/sadanandwargad/libraby_management.git


Features of this project:
    Student:
        1.can view list of all books
        2.can view book content

    Admin can:
        1.login to admin dashboard

        2.add, delete author

        3. Create an entry for Books.

        4. Retrieve all the books.

        5. Update a book.

        6. Delete a book.
________________________________________________________________________________________________________________________

base app:

    This is our main app where we will write our library system's main logic. It comprises of 2 models:

        User - Custome user model for storing email as username & password  of admin user
        Book - for storing name , Author ,category of a book & connecting to the admin

Django rest api:
    2 apis for :
        1.get all books records
        
        2.get single book record