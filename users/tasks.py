from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

@shared_task
def send_email(subject, message, from_email, recipient_list):
    print('here')
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    print('there')

@shared_task
def send_daily_likes_notification():
    yesterday = timezone.now() - timedelta(days=1)
    users = User.objects.filter(recipes__likes__created_at__gte=yesterday).distinct()
    
    for user in users:
        likes_count = user.recipes.filter(likes__created_at__gte=yesterday).count()
        send_email.delay(
            'Daily Likes Notification',
            f'Your recipes received {likes_count} likes yesterday!',
            'from@example.com',
            [user.email]
        )