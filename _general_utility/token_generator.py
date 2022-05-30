from django.db import models
from django.conf import settings
from typing import Type, TypeVar
import os
import binascii


# Generate token
def generate_token(size: int):
    token = binascii.hexlify(os.urandom(size)).decode()
    if len(token) > size:
        return token[0:size].upper()
    else:
        return token.upper()

M = TypeVar('M', bound=models.Model)


# def generate_model_code(cls: Type[M], min_size: int = 5, code_field: str = 'code'):
#     size = min_size
#     code = generate_token(size)
#     while cls.objects.filter(**{code_field: code}).exists():
#         size += 1
#         code = generate_token(size)
#     return code


def generate_model_code(cls: Type[M], min_size: int = 5, code_field: str = 'code'):
    size = min_size
    code = generate_token(size)
    while cls.objects.filter(**{code_field: code}).exists():
        size += 1
        code = generate_token(size)
    return code
# def generate_blog_post_code(model_name: str):
#     return f"{generate_model_code(model_name, 5)}"