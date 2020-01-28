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
    if not 'INSERT' in query:
        rows = crsr.fetchall()
    else:
        rows = None
    description = crsr.description
    crsr.close()
    conn.close()
    return rows , description


def home_page(request):
    return render(request, 'backend/home.html', {})

def donor_info(request):
    national_id = request.GET.get('national_id', None)
    if national_id is None:
        return render(request, 'backend/home.html', {'error': 'لطفاً کد ملی را وارد کنید.'})
    rows, desc = execute(f"SELECT * FROM BloodTransporter WHERE nationalId={national_id}")
    desc = [d[0] for d in desc]
    donor = rows[0]
    print('------------')
    print(rows, desc)
    print('------------')
    return render(request, 'backend/donor_info.html', {'result': donor, 'titles': desc})

def new_donor(request):
    if request.method == 'POST':
        national_id = request.POST.get('nationalId', None)
        first_name = request.POST.get('firstName', None)
        last_name = request.POST.get('lastName', None)
        blood_type = request.POST.get('bloodType', None)
        print(f"'{national_id}' '{first_name}' '{last_name}' '{blood_type}'")
        if '' in [national_id, first_name, last_name, blood_type]:
            return render(request, 'backend/new_donor.html', {'message': 'لطفاً تمامی فیلدهای مربوطه را پر کنید.'})
        try:
            rows, desc = execute(f"INSERT INTO BloodTransporter (nationalId, firstName, lastName, bloodType) VALUES (N'{national_id}', N'{first_name}', N'{last_name}', N'{blood_type}')")
        except pyodbc.IntegrityError:
            return render(request, 'backend/new_donor.html', {'message': 'نع!.'})
        print(rows, desc)
        return render(request, 'backend/home.html', {'message': 'اهداگر جدید با موفقیت اضافه شد.'})
    else:
        return render(request, 'backend/new_donor.html', {})


def necessary_blood_products_in_city(request):
    city_name = request.GET.get('city_name', None)
    blood_type = request.GET.get('blood_type', None)
    if None in [city_name, blood_type]:
        return render(request, 'backend/home.html', {'error': 'لطفاً مقادیر خواسته شده را وارد کنید.'})
    rows, desc = execute(f"EXEC OrderNecessaryBloodProductsInCity @city_name_of_requester = N'{city_name}', @blood_type = N'{blood_type}'")
    print('------------')    
    print(rows)
    print('------------')
    return render(request, 'backend/blood_product_info.html', {'result': rows, 'titles': desc})


def get_blood_transporter_info(request):
    pass
    # execute("")