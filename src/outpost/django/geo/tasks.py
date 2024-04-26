import logging
from datetime import timedelta

from celery import shared_task
from django.utils.translation import gettext_lazy as _
from outpost.django.structure.models import Organization

from .models import Room

logger = logging.getLogger(__name__)


class SynchronizationTasks:
    @shared_task(
        bind=True, ignore_result=True, name=f"{__name__}.Synchronization:rooms"
    )
    def rooms(task):
        rooms = Room.objects.exclude(campusonline__organization=None)
        logger.info("Synchronizing {} geo.Room".format(rooms.count()))
        for r in rooms:
            o = Organization.objects.get(campusonline=r.campusonline.organization)
            r.organization = o
            r.save()
