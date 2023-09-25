from django.db import models

# Create your models here.
class Branch(models.Model):
    branch_name=models.CharField(max_length=30,unique=True)
    branch_link=models.CharField(max_length=200,unique=True)
    class Meta:
        ordering = ('branch_name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'
    def __str__(self):
        return '{}'.format(self.branch_name)

class Sub_branch(models.Model):
    sub_name=models.CharField(max_length=30,unique=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    class Meta:
        ordering = ('sub_name',)
        verbose_name = 'Sub branch'
        verbose_name_plural = 'Sub branches'
    def __str__(self):
        return '{}'.format(self.sub_name)

class Cust_details(models.Model):
    cust_name=models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=300)
    address=models.TextField(blank=True)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    sub_branch = models.ForeignKey(Sub_branch, on_delete=models.CASCADE)
    material = models.CharField(max_length=300)
    account_type = models.CharField(max_length=300)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('cust_name',)
        verbose_name='customer'
        verbose_name_plural='customers'
    def __str__(self):
        return '{}'.format(self.cust_name)




