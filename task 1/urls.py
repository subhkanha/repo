from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.db import connection

# Logic to save user to database.db (db.sqlite3)
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        # This creates the table and saves the data directly
        with connection.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", [name, email])
        
        return render(request, 'index.html', {'msg': 'User saved to db.sqlite3!'})

    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]