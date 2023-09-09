from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
import pymysql

# Create your views here.
def index(request):
    return render(request, 'login_page.html')

def loginsuccess(request):
    login_info = [request.POST['username'], request.POST['password']]
    context = {'data' : select_all_data()}
    if login_info[0] == 'lds961006' and login_info[1] == '635d0b4108':
        return render(request, 'main_page.html', context)
    else:
        return render(request, 'login_page.html')
    
def loginsuccess_test(request):
    login_info = [request.POST['username'], request.POST['password']]
    context = {'data' : select_all_data()}
    if login_info[0] == 'lds961006' and login_info[1] == '635d0b4108':
        return render(request, 'main_page.html', context)
    else:
        return render(request, 'login_page.html')


def select_all_data():
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='mydb', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT c_idx, c_name, c_phone, c_address, c_memo from customer")
    result = cur.fetchall()
    return_data = []

    for idx, value in enumerate(result):
        row = {'c_idx' : value[0],
                       'c_name' : value[1],
                       'c_phone' : value[2],
                       'c_address' : value[3],
                       'c_memo' : value[4]}
        return_data.append(row)

    conn.close()

    return return_data