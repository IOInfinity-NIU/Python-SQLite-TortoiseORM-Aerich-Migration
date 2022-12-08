"""
Title       : Design the product schema of Tortoise ORM
File Name   : orm_schema.py
Create Time : 2022/12/05
Author      : IOInfinity x 源碼無限 
"""


from tortoise import fields
from tortoise.models import Model


class Product(Model):
    """
    Product schema
    """
    id = fields.IntField(pk=True)
    product_name = fields.CharField(max_length=64)
    product_type = fields.CharField(max_length=16)
    base64_image = fields.TextField()

    def __str__(self):
        return self.product_name
