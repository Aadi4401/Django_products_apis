from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Product
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Product)
def product_saved(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Product created: id={instance.id}, title={instance.title}")
    else:
        logger.info(f"Product updated: id={instance.id}, title={instance.title}")

@receiver(post_delete, sender=Product)
def product_deleted(sender, instance, **kwargs):
    logger.info(f"Product deleted: id={instance.id}, title={instance.title}")
