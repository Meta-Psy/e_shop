from django.db import models

class CategoryProduct(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Catygories'

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_cost = models.FloatField()
    product_descr = models.TextField()
    product_image = models.FileField(upload_to='product_image')
    product_count = models.IntegerField(default=0)
    product_category = models.ForeignKey(CategoryProduct,
                                         on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'

class UserCart(models.Model):
    user_id = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id, self.product

    class Meta:
        verbose_name = 'User Cart'
        verbose_name_plural = 'User Carts'