from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='category')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name =models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    
class Dish(models.Model):
        dish_type_choices = (
            ('egg', 'Egg'),
            ('vegan', 'Vegan'),
            
        )
        title = models.CharField(max_length=50)
        image = models.ImageField(upload_to='dish')
        description = models.TextField()
        price = models.DecimalField(max_digits=10, decimal_places=2)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        dish_type = models.CharField(max_length=10, choices=dish_type_choices)
        avaliable = models.BooleanField(default=True)
        best_seller = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title