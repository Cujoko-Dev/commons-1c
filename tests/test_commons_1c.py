# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from six import assertRaisesRegex, assertRegex

from commons_1c.platform_ import get_last_1c_exe_file_path
from commons_1c.version import get_version_as_number, get_version_as_parts
from compat import Path


class MainTestClass(unittest.TestCase):
    def test_get_version_as_number(self):
        self.assertEqual(get_version_as_number(''), 0)
        self.assertEqual(get_version_as_number('foo'), 0)
        self.assertEqual(get_version_as_number('1'), 1000000000000)
        self.assertEqual(get_version_as_number('1.1'), 1000100000000)
        self.assertEqual(get_version_as_number('1.1.1'), 1000100010000)
        self.assertEqual(get_version_as_number('1.1.1.1'), 1000100010001)

    def test_get_version_as_parts(self):
        self.assertEqual(get_version_as_parts(''), [])
        self.assertEqual(get_version_as_parts('foo'), [])
        self.assertEqual(get_version_as_parts('1'), ['1'])
        self.assertEqual(get_version_as_parts('1.1'), ['1', '1'])
        self.assertEqual(get_version_as_parts('1.1.1'), ['1', '1', '1'])
        self.assertEqual(get_version_as_parts('1.1.1.1'), ['1', '1', '1', '1'])

    def test_get_last_1c_exe_file_path_1(self):
        path = get_last_1c_exe_file_path()
        self.assertIsInstance(path, Path)
        assertRegex(self, str(path), r'(?i)c:\\Program Files \(x86\)\\1cv8\\\d+\.\d+\.\d+\.\d+\\bin\\1cv8\.exe')

    def test_get_last_1c_exe_file_path_2(self):
        with assertRaisesRegex(self, Exception, r'1CEStart.cfg file does not exist'):
            get_last_1c_exe_file_path(config_file='bla.cfg')
