from utils.email_sender import send_email
from utils.whatsapp import send_whatsapp

def notify_low_stock(product, email=None, phone=None):
    msg = f"⚠ LOW STOCK ALERT\nProduct: {product.product_name}\nSKU: {product.sku}\nStock: {product.quantity}"
    if email:
        send_email(email, "Low Stock Alert", msg)
    if phone:
        send_whatsapp(phone, msg)

def notify_expiry(product, email=None):
    msg = f"⚠ EXPIRY ALERT\nProduct {product.product_name} (SKU {product.sku}) is nearing expiry!"
    if email:
        send_email(email, "Expiry Alert", msg)

def notify_supplier_issue(supplier, email=None):
    msg = f"⚠ SUPPLIER ISSUE\nSupplier {supplier.name} rating dropped to {supplier.rating}"
    if email:
        send_email(email, "Supplier Rating Alert", msg)
