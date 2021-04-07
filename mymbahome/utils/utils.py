from projects.models import ModelActivity


def get_total_impacted_animals():
    try:
        count = 0
        for activity in ModelActivity.objects.all().exclude(type="deleted"):
            count += activity.impacted_animals
        return count
    except:
        return 0
