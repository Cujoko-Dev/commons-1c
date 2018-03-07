# -*- coding: utf-8 -*-
from pathlib import Path
import unittest

from commons_1c import get_last_1c_exe_file_path, get_version_as_number, get_version_as_parts


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

    def test_get_last_1c_exe_file_path(self):
        path = get_last_1c_exe_file_path()
        self.assertIsInstance(path, Path)
        self.assertRegex(str(path), r'c:\\Program Files \(x86\)\\1cv8\\\d+\.\d+\.\d+\.\d+\\bin\\1cv8\.exe')
