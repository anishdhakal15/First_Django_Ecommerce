from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=355)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default='')

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
        

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items = models.CharField(max_length=10000)
    name = models.CharField(max_length=90)
    amount = models.IntegerField(default=0)
    email = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=700, default="")
    state = models.CharField(max_length=500, default="")
    zipcode = models.CharField(max_length=50, default="")
    address1 = models.CharField(max_length=500, default="")
    address2 = models.CharField(max_length=500, default="")
    phone = models.CharField(max_length=15, default="")
    def __str__(self):
        return self.name
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=10000)
    update_desc = models.CharField(max_length=90)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+'...'
        
    