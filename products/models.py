from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    ssn = models.CharField(max_length=20) 
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # soft delete helper
    def soft_delete(self):
        self.is_active = False
        self.save(update_fields=["is_active"])

    def __str__(self):
        return self.title


@receiver(post_save, sender=Product)
def product_saved(sender, instance, created, **kwargs):
    if created:
        print(f"[SIGNAL] Product created: {instance.title}")
    else:
        print(f"[SIGNAL] Product updated: {instance.title}")