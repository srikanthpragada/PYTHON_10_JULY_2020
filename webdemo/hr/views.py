from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


def index(request):
    return HttpResponse("<h1>Human Resource Application</h1>")


def about(request):
    return render(request, 'about.html',
                  {
                      'title': 'HR Application',
                      'tasks': ['Adding Employee', 'Updating Salary', 'Listing Employees']
                  }
                  )


def list_employees(request):
    con = sqlite3.connect(r"c:\classroom\july10\hr.db")
    cur = con.cursor()
    cur.execute("select * from employees")
    employees = cur.fetchall()
    con.close()

    return render(request, 'list_employees.html', {'employees': employees})
