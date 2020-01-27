from django.shortcuts import render
import pyodbc
from django.db import connection

def execute(query):
    server= 'ZENBOOK'
    db = 'BloodTransfusion'
    username = 'dblab'
    password = 'fV5S7H3jt247'
    # conn = pyodbc.connect(f'Driver={{SQL Server}};Server={server};Database={db};UID={username};PWD={password};Trusted_Connection=no;')

    conn = pyodbc.connect(f'Driver={{SQL Server}};Server={server};Database={db};Trusted_Connection=yes;')
    crsr = conn.cursor()
    crsr.execute(query)
    rows = crsr.fetchall()
    description = crsr.description
    crsr.close()
    conn.close()
    return rows , description


def home_page(request):
    return render('backend/home.html', {})

def list_blood_transporters(request):
    print("Yay")
    # cursor = connection.cursor()
    # cursor.execute("EXEC ListBloodTransporters")
    rows, desc = execute("EXEC ListBloodTransporters")
    print('------------')
    print(rows, desc)
    print('------------')
    # return render('backend/list_blood_transporters.html', rows)


def get_blood_transporter_info(request):
    pass
    # execute("")