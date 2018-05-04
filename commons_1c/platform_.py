# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from appdirs import site_data_dir

from commons.compat import Path
from commons_1c.version import get_version_as_number


def get_last_1c_exe_file_path(**kwargs):
    result = None
    if 'config_file' in kwargs:
        config_file_path = Path(kwargs['config_file'])
    else:
        config_file_path = Path(site_data_dir('1CEStart', '1C')) / '1CEStart.cfg'
    if config_file_path.is_file():
        installed_location_paths = []
        with config_file_path.open(encoding='utf-16') as config_file:
            for line in config_file.readlines():
                key_and_value = line.split('=')
                if key_and_value[0] == 'InstalledLocation':
                    value = '='.join(key_and_value[1:])
                    installed_location_paths.append(Path(value.rstrip('\r\n')))
        platform_versions = []
        for installed_location_path in installed_location_paths:
            if installed_location_path.is_dir():
                for version_dir_path in installed_location_path.iterdir():
                    version_as_number = get_version_as_number(str(version_dir_path.name))
                    if version_as_number:
                        exe_file_path = version_dir_path / 'bin' / '1cv8.exe'
                        if exe_file_path.is_file():
                            platform_versions.append((version_as_number, exe_file_path))
        platform_versions_reversed = sorted(platform_versions, key=lambda x: x[0], reverse=True)
        if platform_versions_reversed:
            result = platform_versions_reversed[0][1]
    else:
        raise FileNotFoundError('1CEStart.cfg file does not exist')
    return result
