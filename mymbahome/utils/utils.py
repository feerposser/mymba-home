from projects.models import ModelActivity


def get_total_impacted_animals():
    try:
        count = 0
        for activity in ModelActivity.objects.all():
            count += activity.impacted_animals
        return count
    except Exception as e:
        print(e)
