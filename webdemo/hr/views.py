from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3
import requests
from .forms import EmployeeForm


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
            con.commit()
            msg = "Updated Employee Successfully!"
        else:
            msg = "Employee Id Not Found!"

        return render(request, 'update_salary.html',
                      {'message': msg, 'id': id, 'salary': salary})

    return render(request, 'update_salary.html')


def add_employee(request):
    if request.method == "GET":
        ef = EmployeeForm()  # Empty form
        return render(request, 'add_employee.html', {'form': ef})
    else:  # POST
        ef = EmployeeForm(request.POST)  # bind request data with form
        if ef.is_valid():
            name = ef.cleaned_data['name']
            job = ef.cleaned_data['job']
            salary = ef.cleaned_data['salary']
            # Insert row into EMPLOYEES table
            con = sqlite3.connect(r"c:\classroom\july10\hr.db")
            cur = con.cursor()
            try:
                cur.execute("insert into employees(name,job,salary) values(?,?,?)", (name, job, salary))
                msg = f"Employee {name} was added successfully!"
                con.commit()
                return redirect("/hr/employees/")
            except Exception as ex:
                print("Error in add_employee :", ex)
                msg = "Sorry! Could not add employee due to error!"
            finally:
                con.close()
        else:
            msg = "Invalid Data. Please correct and resubmit!"

        return render(request, 'add_employee.html', {'form': ef, 'message': msg})
