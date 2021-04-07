from django.db.models.signals import post_save, post_delete, pre_delete
from django.core.cache import cache
import os

from .models import ModelActivity
from utils.utils import get_total_impacted_animals


def impacted_animals_updated_cache_update(sender, **kwargs):
    """
    Called when an Activity is created or updated. This function allow the cache used to hadle the number of
    impacted animals to be updated by using updated data.
    :return: None
    """
    impacted_animals_updated = get_total_impacted_animals()
    cache.set("impacted_animals", impacted_animals_updated)


def activity_deleted_remove_images(sender, instance, **kwargs):
    """
    Called when a activity is being deleted (before deletion). This functions remove the images related with
    the Activity instance if aren't being used by another activity.
    :param sender: Model Activity
    :param instance: Activity instance deleted
    :param kwargs:
    :return: None
    """
    try:
        for image in instance.images.all():
            if sender.objects.filter(images__image=image).count() == 1:
                if os.path.isfile(image.image.path):
                    os.remove(image.image.path)
                image.delete()
            else:
                print("Not be able to delete. Image %s exists in some other instance." % image)
    except Exception as e:
        print("---->", e)


post_save.connect(impacted_animals_updated_cache_update, sender=ModelActivity)
post_delete.connect(impacted_animals_updated_cache_update, sender=ModelActivity)
pre_delete.connect(activity_deleted_remove_images, sender=ModelActivity)
