from celery import shared_task

from posts.services import send_mails_to_followers


@shared_task
def send_mails(post_id):
    send_mails_to_followers(post_id)
