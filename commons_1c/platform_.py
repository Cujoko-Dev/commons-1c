# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import errno
import os

from appdirs import site_data_dir

from commons_1c.version import get_version_as_number


def get_last_1c_exe_file_fullname(**kwargs):
    result = None
    if 'config_file' in kwargs:
        # todo Может быть относительный путь
        config_file_fullname = kwargs['config_file']
    else:
        config_file_fullname = os.path.join(site_data_dir('1CEStart', '1C'), '1CEStart.cfg')
    if os.path.isfile(config_file_fullname):
        installed_location_fullnames = []
        with open(config_file_fullname) as config_file:
            for line in config_file.readlines():
                # fixme Наверное, неправильная работа с кодировкой
                key_and_value = line.decode('utf-16').split('=')
                if key_and_value[0] == 'InstalledLocation':
                    value = '='.join(key_and_value[1:])
                    installed_location_fullnames.append(value.rstrip('\r\n'))
        platform_versions = []
        for installed_location_fullname in installed_location_fullnames:
            if os.path.isdir(installed_location_fullname):
                for version_dir_shortname in os.listdir(installed_location_fullname):
                    version_dir_fullname = os.path.join(installed_location_fullname, version_dir_shortname)
                    version_as_number = get_version_as_number(version_dir_shortname)
                    if version_as_number:
                        exe_file_fullname = os.path.join(version_dir_fullname, 'bin', '1cv8.exe')
                        if os.path.isfile(exe_file_fullname):
                            platform_versions.append((version_as_number, exe_file_fullname))
        platform_versions_reversed = sorted(platform_versions, key=lambda x: x[0], reverse=True)
        if platform_versions_reversed:
            result = platform_versions_reversed[0][1]
    else:
        raise IOError(errno.ENOENT, '1CEStart.cfg file does not exist')
    return result
