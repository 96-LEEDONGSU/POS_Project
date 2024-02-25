from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
import pymysql

# Create your views here.
def index(request):
    return render(request, 'login_page.html')

def loginsuccess(request):
    login_info = [request.POST['username'], request.POST['password']]
    context = {'data' : select_all_data()}
    if login_info[0] == 'lds961006' and login_info[1] == '635d0b4108':
        return render(request, 'customer_list.html', context)
    else:
        return render(request, 'login_page.html')

def productlist(request):
    context = {'data' : select_product_list()}
    return render(request, 'product_list.html', context)


def customerlist(request):
    context = {'data' : select_all_data()}
    return render(request, 'customer_list.html', context)


def customer_modify(request, id):
    context = {'data1' : id, 'data2' : select_all_data()}
    return render(request, 'customer_modify.html', context)

def customer_add(request):
    return render(request, 'add_member.html')
        

def select_product_list():
    conn = pymysql.connect(host='localhost', user='root', password='635d0b4108', db='mydb', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT Product_name, Shop_Product_saleprice, Shop_Product_purchaseprice, Shop_Product_purchasedate, Shop_Product_purchase_route, Product_Code, Shop_Product_stockcount from shop_product")
    result = cur.fetchall()
    return_data = []
    
    for idx, value in enumerate(result):
        row = {'Product_name' : value[0],
                       'Shop_Product_saleprice' : value[1],
                       'Shop_Product_purchaseprice' : value[2],
                       'Shop_Product_purchase_route' : value[3],
                       'Product_Code' : value[4],
                       'Shop_Product_stockcount' : value[5]}
        return_data.append(row)
    conn.close()
    return return_data


def select_all_data():
    conn = pymysql.connect(host='localhost', user='root', password='635d0b4108', db='mydb', charset='utf8')
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

#login_info = [request.POST['username'], request.POST['password']]

def modifyMemberData(request):
    modify_data = [request.POST['c_name'], request.POST['c_phone'], request.POST['c_address'], request.POST['c_memo'], request.POST['c_idx']]
    conn = pymysql.connect(host='localhost', user='root', password='635d0b4108', db='mydb', charset='utf8')
    cur = conn.cursor()
    sql = f"UPDATE customer SET c_name = \'{modify_data[0]}\', c_phone = \'{modify_data[1]}\', c_address = \'{modify_data[2]}\', c_memo = \'{modify_data[3]}\' WHERE c_idx = {modify_data[4]};"
    cur.execute(sql)
    conn.commit()
    conn.close()
    context = {'data' : select_all_data()}
    return render(request, 'customer_list.html', context)

def addMember(request):
    modify_data = [request.POST['c_name'], request.POST['c_phone'], request.POST['c_address'], request.POST['c_memo']]
    conn = pymysql.connect(host='localhost', user='root', password='635d0b4108', db='mydb', charset='utf8')
    cur = conn.cursor()
    sql = f"INSERT INTO customer(c_name, c_phone, c_address, c_memo) VALUES (\'{modify_data[0]}\', \'{modify_data[1]}\', \'{modify_data[2]}\', \'{modify_data[3]}\')"
    cur.execute(sql)
    conn.commit()
    conn.close()
    context = {'data' : select_all_data()}
    return render(request, 'customer_list.html', context)