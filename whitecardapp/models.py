from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    phone_no = models.IntegerField()
    Gender = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    aadhar_no = models.IntegerField()
    license_no = models.IntegerField()
    electionid_no = models.CharField(max_length=15)
    rationcard_no = models.IntegerField()
    Photo = models.ImageField(upload_to="usr_photo")
    rto_approval = models.CharField(max_length=10, default=False)
    ration_approval = models.CharField(max_length=10, default=False)
    voter_approval = models.CharField(max_length=10, default=False)
    admin_approval = models.CharField(max_length=10, default=False)
    it_return_approval = models.CharField(max_length=10, default=False)
    qr = models.ImageField(upload_to='qr_code', null=True)
    applicant = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return self.name
        






