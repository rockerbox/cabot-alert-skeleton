from django.db import models

from cabot.cabotapp.alert import AlertPlugin
from cabot.cabotapp.alert import AlertPluginUserData

import requests
import json

from logging import getLogger
logger = getLogger(__name__)

class WebhookAlert(AlertPlugin):
    name = "Webhook"
    slug = "cabot_alert_webhook"
    author = "Rockerbox"
    version = "0.0.1"
    font_icon = "fa fa-rocket"

    def send_alert(self, service, users, duty_officers):
        payload = {
            'service': service.name,
            'status': service.overall_status,
            'old_status': service.old_overall_status,
        }

        webhook_urls = [u.webhook_url for u in WebhookAlertUserData.objects.filter(user__user__in=users)]

        for url in webhook_urls:
            logger.info(message)
            requests.post(
                url,
                data=json.dumps(payload)
            )
        return True

class WebhookAlertUserData(AlertPluginUserData):
    name = "Webhook Plugin"
    webhook_url = models.URLField(max_length=200, blank=True)
