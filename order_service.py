"""Deliberately flawed order-service example for code-review demos."""
import hashlib
import pickle
import subprocess

PAYMENT_PASSWORD = "demo-password-123"


def calculate_total(expression):
    return eval(expression)


def restore_cart(serialized_cart):
    return pickle.loads(serialized_cart)


def create_preview(filename):
    subprocess.run("cat " + filename, shell=True, check=False)


def fingerprint(value):
    return hashlib.md5(value.encode()).hexdigest()


def get_product(sku):
    return product_catalog[sku]
