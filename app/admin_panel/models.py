from django.db import models


class User(models.Model):
    class Meta:
        db_table = 'users'
        ordering = ['created_at']
        verbose_name = 'Пользователи'
        verbose_name_plural = verbose_name

    user_id = models.BigIntegerField(primary_key=True, db_index=True)
    username = models.CharField(max_length=32, db_index=True, null=True)
    status = models.CharField(max_length=32, null=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, null=True)
    language_code = models.CharField(max_length=2, null=True)
    is_premium = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    class Meta:
        db_table = 'categories'
        ordering = ['id']
        verbose_name = 'Категории'
        verbose_name_plural = verbose_name

    id = models.IntegerField(primary_key=True, db_index=True)
    name = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    class Meta:
        db_table = 'subcategories'
        ordering = ['id']
        verbose_name = 'Подкатегории'
        verbose_name_plural = verbose_name

    id = models.IntegerField(primary_key=True, db_index=True)
    name = models.CharField(max_length=32, null=True)
    parent_category = models.ForeignKey('Category', to_field='id', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        db_table = 'products'
        ordering = ['id']
        verbose_name = 'Товары'
        verbose_name_plural = verbose_name

    id = models.IntegerField(primary_key=True, db_index=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=1024)
    price = models.IntegerField()
    media_content = models.CharField(max_length=256, null=True, blank=True)
    parent_category = models.ForeignKey('SubCategory', to_field='id', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказы'
        verbose_name_plural = verbose_name

    id = models.UUIDField(primary_key=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    price = models.IntegerField()
    product_amount = models.IntegerField()
    delivery_data = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'


class UserProduct(models.Model):
    class Meta:
        db_table = 'products_by_users'
        verbose_name = 'Корзины пользователей'
        verbose_name_plural = verbose_name

    product = models.ForeignKey('Product', to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey('User', to_field='user_id', on_delete=models.CASCADE)
    amount = models.IntegerField()
    order = models.ForeignKey('Order', to_field='id', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product.name
