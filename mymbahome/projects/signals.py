from django.db.models.signals import post_save, post_delete
from django.core.cache import cache

from .models import ModelActivity
from utils.utils import get_total_impacted_animals


def impacted_animals_created_or_updated_cache_update(sender, **kwargs):
    """
    Called when an Activity is created or updated. This function allow the cache used to hadle the number of
    impacted animals to be updated by using updated data.
    :return: None
    """
    impacted_animals_updated = get_total_impacted_animals()
    cache.set("impacted_animals", impacted_animals_updated)


def impacted_animals_deleted_cache_update(sender, instance, **kwargs):
    """
    Called when an Activity is deleted. This function allow the cache used to handle the number of
    impacted animals to be update by using updated data.
    :param sender: Model
    :param instance: Model objected being deleted
    :param kwargs:
    :return: Nome
    """
    impacted_animals_updated = cache.get("impacted_animals", get_total_impacted_animals()) - instance.impacted_animals
    cache.set("impacted_animals", impacted_animals_updated)


post_save.connect(impacted_animals_created_or_updated_cache_update, sender=ModelActivity)
post_delete.connect(impacted_animals_deleted_cache_update, sender=ModelActivity)
