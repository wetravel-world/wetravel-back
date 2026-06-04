from celery import shared_task
from django.db.models import Avg


@shared_task
def recalculate_city_score(city_id):
    from .models import City, Comment
    try:
        city = City.objects.get(pk=city_id)
    except City.DoesNotExist:
        return

    approved = Comment.objects.filter(city=city, is_approved=True)
    result = approved.aggregate(avg=Avg('score'))
    city.welcome_score = result['avg'] or 0.0
    city.score_count = approved.count()
    city.save(update_fields=['welcome_score', 'score_count'])
