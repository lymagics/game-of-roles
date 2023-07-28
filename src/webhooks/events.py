from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

import stripe
from djstripe import webhooks

from roles.models import Role, Subscription
from users.models import User

if settings.DEBUG:
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
else:
    stripe.api_key = settings.STRIPE_LIVE_SECRET_KEY


@webhooks.handler('checkout.session.completed')
def stripe_webhook(event, **kwargs):
    session = stripe.checkout.Session.retrieve(
        event.data['object']['id'],
    )

    user_id = session.metadata['user_id']
    name = session.metadata['role']
    interval = session.metadata['interval']
    subscription = session.subscription
    user = get_object_or_404(User, pk=user_id)
    role = get_object_or_404(Role, name=name)

    Subscription.objects.create(
        ref=subscription, interval=interval,
        user=user, role=role,
    )
    return HttpResponse('', status=200)
