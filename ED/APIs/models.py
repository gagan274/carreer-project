from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    grant_type = models.CharField(max_length=50)
    time = models.DecimalField(max_digits=50, decimal_places=0)
    token = models.CharField(max_length=150)
    remember_me = models.BooleanField(default=False)
    class Meta:
        managed = False
        db_table = 'login'
        unique_together = (('username'),)


class Register(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phonenumber = models.IntegerField()
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    profilephoto = models.CharField(max_length=5000)
    timestamp = models.DecimalField(max_digits=50, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'register'  # Assuming 'register' is the correct table name
        unique_together = (('email', 'phonenumber'),)  # Example: Ensure email and phonenumber combination is unique

class OTP(models.Model):
    email = models.CharField(max_length=50)
    otp = models.CharField(max_length=5)
    timestamp = models.DecimalField(max_digits=50, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'otp'
        unique_together = (('otp'),)
