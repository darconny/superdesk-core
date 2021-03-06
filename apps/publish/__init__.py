# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

import logging
from superdesk import get_backend
import superdesk

from apps.publish.content import ArchivePublishResource, ArchivePublishService, \
    KillPublishResource, KillPublishService, CorrectPublishResource, CorrectPublishService, \
    ResendResource, ResendService, TakeDownPublishService, TakeDownPublishResource, \
    UnpublishResource, UnpublishService
from apps.publish.enqueue import EnqueueContent
from apps.publish.published_item import PublishedItemResource, PublishedItemService
from apps.publish.content.published_package_items import PublishedPackageItemsService,\
    PublishedPackageItemsResource


logger = logging.getLogger(__name__)


def init_app(app):

    endpoint_name = 'archive_publish'
    service = ArchivePublishService(endpoint_name, backend=get_backend())
    ArchivePublishResource(endpoint_name, app=app, service=service)

    endpoint_name = 'archive_kill'
    service = KillPublishService(endpoint_name, backend=get_backend())
    KillPublishResource(endpoint_name, app=app, service=service)

    endpoint_name = 'archive_correct'
    service = CorrectPublishService(endpoint_name, backend=get_backend())
    CorrectPublishResource(endpoint_name, app=app, service=service)

    endpoint_name = 'archive_takedown'
    service = TakeDownPublishService(endpoint_name, backend=get_backend())
    TakeDownPublishResource(endpoint_name, app=app, service=service)

    endpoint_name = 'published'
    service = PublishedItemService(endpoint_name, backend=get_backend())
    PublishedItemResource(endpoint_name, app=app, service=service)

    endpoint_name = 'archive_resend'
    service = ResendService(endpoint_name, backend=get_backend())
    ResendResource(endpoint_name, app=app, service=service)

    endpoint_name = 'published_package_items'
    service = PublishedPackageItemsService(endpoint_name, backend=get_backend())
    PublishedPackageItemsResource(endpoint_name, app=app, service=service)

    endpoint_name = 'archive_unpublish'
    service = UnpublishService(endpoint_name, backend=get_backend())
    UnpublishResource(endpoint_name, app=app, service=service)

    superdesk.privilege(name='subscribers', label='Subscribers', description='User can manage subscribers')
    superdesk.privilege(name='publish', label='Publish', description='Publish a content')
    superdesk.privilege(name='kill', label='Kill', description='Kill a published content')
    superdesk.privilege(name='correct', label='Correction', description='Correction to a published content')
    superdesk.privilege(name='publish_queue', label='Publish Queue', description='User can update publish queue')
    superdesk.privilege(name='resend', label='Resending Stories', description='User can resend published stories')
    superdesk.privilege(name='embargo', label='Embargo', description='User can set embargo date')
    superdesk.privilege(name='takedown', label='Take down', description='Take down a published content')
    superdesk.privilege(name='unpublish', label='Unpublish', description='Unpublish a published content')


def enqueue_content():
    EnqueueContent().run()
