from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector as conn


def index(request):
    try:
        database = conn.connect(host="127.0.0.1",
                            database="new2",
                            user="root",
                            password="root")

        c = database.cursor()
        query = f"SELECT * FROM catalog"
        c.execute(query)
        content = c.fetchall()

    except Exception as e:
        pass
    return render(request,"category.html",{'products':content})


def details(request,product_id):

    try:
        database = conn.connect(host="127.0.0.1",
                            database="new2",
                            user="root",
                            password="root")

        c = database.cursor()
        query = f"SELECT * FROM catalog WHERE id = {int(product_id)}"
        c.execute(query)
        content = c.fetchall()

    except Exception as e:
        pass
    return render(request,"single-product.html",{'product_data':content[0]})
