# -*- coding: utf-8 -*-

import unittest

from zope.component import queryUtility, getMultiAdapter

from plone.registry.interfaces import IRegistry

from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from collective.analyticspanel.interfaces import IAnalyticsSettings
from collective.analyticspanel.testing import ANALYTICS_PANEL_INTEGRATION_TESTING

from base import BaseTestCase

class TestConfiguration(BaseTestCase):

    layer = ANALYTICS_PANEL_INTEGRATION_TESTING

    def test_default_configuration(self):
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IAnalyticsSettings, check=False)
        self.assertEqual(settings.general_code, 'SITE DEFAULT ANALYTICS')

    def test_hidden_plone_base_analytics(self):
        portal = self.layer['portal']
        self.markRequestWithLayer()
        setRoles(portal, TEST_USER_ID, ['Member', 'Manager'])
        request = self.layer['request']
        controlpanel_view = getMultiAdapter((portal, request), name=u'site-controlpanel')
        self.assertTrue('form.webstats_js' not in controlpanel_view())
