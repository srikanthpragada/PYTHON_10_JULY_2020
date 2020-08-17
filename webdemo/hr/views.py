from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import requests


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


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    return render(request, 'list_countries.html', {'countries': countries})


def update_salary(request):
    if 'id' in request.POST:  # data is present
        # process data
        id = request.POST['id']
        salary = request.POST['salary']
        # update database
        con = sqlite3.connect(r"c:\classroom\july10\hr.db")
        cur = con.cursor()
        cur.execute("update employees set salary = ? where id = ?", (salary, id))
        if cur.rowcount == 1:
            msg = "Updated Employee Successfully!"
        else:
            msg = "Employee Id Not Found!"

        return render(request, 'update_salary.html',
                      {'message': msg, 'id' : id, 'salary' : salary})

    return render(request, 'update_salary.html')
