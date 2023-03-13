from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from whitecardapp.forms import Applicationform
from whitecardapp.models import Application
from .decorator import Admin_only
from django.contrib.auth.models import Group

import qrcode
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('usr_login')
        else:
            messages.info(request, "")
            return redirect('register')
    return render(request, 'register.html')

def usr_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return redirect('usr_login')
    return render(request, 'usr_login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

@Admin_only
def home(request):
    context = request.user
    return render(request, 'home.html', {'context':context})

def application(request):
    if request.method == 'POST':
        form = Applicationform(request.POST, request.FILES)
        if form.is_valid:
            a_no = request.POST.get('aadhar_no')
            app_user = Application.objects.filter(aadhar_no = a_no)
            if app_user.exists():
                error_message = "This Aadhar number has already been submitted."
                return render(request, 'applicationerror.html', {'error_message':error_message})
            else:
                appl = form.save()
                appl.applicant = request.user
                appl.save()
                return redirect('card_status')
        else:
            return HttpResponse(request, 'form is not valid Please fill correctly')
    return render(request, 'application.html', {'form':Applicationform})

def usr_app_del(request, id):
    app_del = Application.objects.filter(id = id)
    app_del.delete()
    return render(request, 'home.html')
        

def card_status(request):
    app_user = Application.objects.filter(applicant=request.user)
    return render(request, 'card_status.html', {'app_user':app_user})

def rto(request):
    app_rto = Application.objects.all()
    if request.method == 'POST':
        try:
            aadhar_no = request.POST.get('aadhar_no')
            rto_user = True
            usr_det = Application.objects.get(aadhar_no = aadhar_no)
            return render(request, 'userdetails.html', {'usr_det':usr_det, 'rto_user':rto_user})
        except:
            return HttpResponse("The Aadhar Number Is Invalid Not Present In Database")
    return render(request, 'rto.html', {'app_rto':app_rto})


def rtoapprove(request,id):
    rto_app = Application.objects.get(id=id)
    if request.method == 'POST':
        approve = request.POST.get("rtoapprove")
        rto_app.rto_approval = approve
        rto_app.save()
        return redirect("rto")
    return render(request, 'rtoapprove.html', {'rto_app':rto_app})


def ration(request):
    app_ration = Application.objects.all()

    if request.method == 'POST':
        try:
            aadhar_no = request.POST.get('aadhar_no')
            ration_user = True
            usr_det = Application.objects.get(aadhar_no = aadhar_no)
            return render(request, 'userdetails.html', {'usr_det':usr_det, 'ration_user':ration_user})
        except:
            return HttpResponse("The Aadhar Number Is Invalid Not Present In Database")

    return render(request, 'Ration.html', {'app_ration':app_ration})

def rationapprove(request,id):
    ration_app = Application.objects.get(id=id)
    if request.method == 'POST':
        approve = request.POST.get("rationapprov")
        ration_app.ration_approval = approve
        ration_app.save()
        return redirect('ration')
    return render(request, 'rationapprove.html', {'ration_app':ration_app})

def it_return(request):
    app_it = Application.objects.all()
    if request.method == 'POST':
        try:
            aadhar_no = request.POST.get('aadhar_no')
            it_user = True
            usr_det = Application.objects.get(aadhar_no = aadhar_no)
            return render(request, 'userdetails.html', {'usr_det':usr_det, 'it_user':it_user})
        except:
            return HttpResponse("The Aadhar Number Is Invalid Not Present In Database")
    return render(request, 'it_return.html', {'app_it':app_it})

def it_return_approve(request,id):
    it_app = Application.objects.get(id=id)
    if request.method == 'POST':
        approve = request.POST.get("itapprov")
        it_app.it_return_approval = approve
        it_app.save()
        return redirect('it_return')
    return render(request, 'it_returnapprove.html', {'it_app':it_app})

def voter(request):
    app_voter = Application.objects.all()

    if request.method == 'POST':
        try:
            aadhar_no = request.POST.get('aadhar_no')
            voter_user = True
            usr_det = Application.objects.get(aadhar_no = aadhar_no)
            return render(request, 'userdetails.html', {'usr_det':usr_det, 'voter_user':voter_user})
        except:
            return HttpResponse("The Aadhar Number Is Invalid Not Present In Database")

    return render(request, 'voter.html', {'app_voter':app_voter})

def voterapprove(request,id):
    voter_app = Application.objects.get(id=id)
    if request.method == 'POST':
        approve = request.POST.get("voterapprov")
        voter_app.voter_approval = approve
        voter_app.save()
        return redirect('voter')
    return render(request, 'voterapprove.html', {'voter_app':voter_app})

def system_admin(request):
    app_admin = Application.objects.all()
    if request.method == 'POST':
        try:
            aadhar_no = request.POST.get('aadhar_no')
            admin_user = True
            usr_det = Application.objects.get(aadhar_no = aadhar_no)
            return render(request, 'userdetails.html', {'usr_det':usr_det, 'admin_user':admin_user})
        except:
            return HttpResponse("The Aadhar Number Is Invalid Not Present In Database")
    return render(request, 'system_admin.html', {'app_admin':app_admin})

def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format='JPEG')
    buffer.seek(0)
    image_file = InMemoryUploadedFile(buffer, None, 'qr.jpg', 'image/jpeg', buffer.getbuffer().nbytes, None)
    return image_file

def adminapprove(request, id):
    admin_app = Application.objects.get(id=id)
    if request.method == 'POST':
        if admin_app.rto_approval =="True" and admin_app.ration_approval =="True" and admin_app.voter_approval =="True" and admin_app.it_return_approval =="True":
            approve = request.POST.get("adminapprov")
            admin_app.admin_approval = approve
            admin_app.save()
            # generate QR code with all the data
            qr_data = f"Name: {admin_app.name}\nFather's Name: {admin_app.father_name}\nPhone Number: {admin_app.phone_no}\nGender: {admin_app.Gender}\nEmail: {admin_app.email}\nDate of Birth: {admin_app.dob}\nAddress: {admin_app.address}\nAadhar Number: {admin_app.aadhar_no}\nLicense No: {admin_app.license_no}\nElection ID No: {admin_app.electionid_no}\nRation Card No: {admin_app.rationcard_no}"
            img = qrcode.make(qr_data)
            # save QR code to model
            qr_code_image = BytesIO()
            img.save(qr_code_image, format='JPEG')
            qr_code_image.seek(0)
            admin_app.qr.save('qr_code.jpg', InMemoryUploadedFile(qr_code_image, None, 'qr_code.jpg', 'image/jpeg', qr_code_image.tell(), None))
            return redirect('system_admin')
        else:
            return HttpResponse("Some Approvals are Pending You Can Check With Aadhar number")
    return render(request, 'adminapprove.html', {'admin_app':admin_app})

def admin_module_create(request):
    app_admin = Application.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')
        module = request.POST.get('module')  
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username Already Exist")
            else:
                user = User.objects.create_user(username=username, password=password)
                group = Group.objects.get(name=module)  
                user.groups.add(group)  
                user.save()
                message = "Successfuly Created"
                return render(request, 'system_admin.html', {'message':message, 'app_admin':app_admin})
        else:
            return HttpResponse("Password Does Not Maching")
        
    return render(request, 'register.html')

def admin_update(request, id):
    admin_app =Application.objects.get(id=id)
    if request.method == 'POST':
        admin_app.name = request.POST.get('name')
        admin_app.last_name = request.POST.get('last_name')
        admin_app.father_name = request.POST.get('father_name')
        admin_app.phone_no = request.POST.get('phone_no')
        admin_app.Gender = request.POST.get('Gender')
        admin_app.email = request.POST.get('email')
        admin_app.dob = request.POST.get('dob')
        admin_app.address = request.POST.get('address')
        admin_app.aadhar_no = request.POST.get('aadhar_no')
        admin_app.license_no = request.POST.get('license_no')
        admin_app.electionid_no = request.POST.get('electionid_no')
        admin_app.rationcard_no = request.POST.get('rationcard_no')
        admin_app.save()
        return redirect('system_admin')
    return render(request, "admin_update.html", {'admin_app':admin_app})

def delete_dep(request):
    app_admin = Application.objects.all()
    if request.method == "POST":
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            user.delete()
            message = f"Successfuly Deleted '{username}'"
            return render(request, 'system_admin.html', {'message':message})
        except User.DoesNotExist:
            message_fail = f"'{username}'Is Not a User Please Check"
            return render(request, 'system_admin.html', {'message_fail':message_fail, 'app_admin':app_admin})