from django.db import models

# Create your models here.
class pzzle(models.Model):
    name = models.CharField(max_length=30, verbose_name="название")
    detail = models.IntegerField(verbose_name="деталей")
    style = models.CharField(max_length=30, verbose_name="стиль")
    material = models.CharField(max_length=30, verbose_name="материал")
    age = models.IntegerField(verbose_name="возраст")
    price = models.IntegerField(verbose_name="цена")
    count = models.IntegerField(verbose_name="количество")
    pic = models.ImageField(upload_to="app1/static/img", blank=True)
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE, default=1)
    size = models.ForeignKey('size', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class size(models.Model):
    size_name = models.CharField(max_length=30)
    size_height = models.CharField(max_length=30)
    size_width = models.CharField(max_length=30)
    
    def __str__(self):
        return self.size_name


class Producer(models.Model):
    producer_name = models.CharField(max_length=100)
    producer_country = models.CharField(max_length=100)
    producer_leval = models.IntegerField()
    producer_img = models.ImageField(upload_to="app1/static/img/producer", blank=True)

    
    def __str__(self):
        return self.producer_name

# class Order(models.Model):
#     # order_number = models.AutoField()
#     order_product = 
#     order_sum = models.IntegerField()

# class line(models.Model):
#     order_number = 
#     product = 
#     line_count = 

class Animal(models.Model):
    name = models.CharField(max_length=10)
    sound = models.CharField(max_length=10)

    def speak(self, a):
        return self.sound * a
    
    def count(self, a):
        return a**2
    
    def meat(self, a):
        return f'nead {a**2}kg meat!'