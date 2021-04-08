from projects.models import ModelActivity


def get_total_impacted_animals():
    try:
        count = 0
        for activity in ModelActivity.objects.all().exclude(type__type="deleted"):
            if activity.impacted_animals:
                count += activity.impacted_animals
        return count
    except Exception as e:
        print(e)
        return 0
