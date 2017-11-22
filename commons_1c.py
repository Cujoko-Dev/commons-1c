#! python3.6
# -*- coding: utf-8 -*-
import re
from pathlib import Path

from appdirs import site_data_dir

__version__ = '1.0.0'

pattern_version = re.compile(r'\D*(?P<version>(\d+)\.(\d+)\.(\d+)\.(\d+))\D*')


def get_version_as_number(version: str):
    result = 0
    m = 10000
    match = pattern_version.match(version)
    if match is not None:
        result = \
            int(match.group(2)) * m ** 3 + \
            int(match.group(3)) * m ** 2 + \
            int(match.group(4)) * m + \
            int(match.group(5))

    return result


def get_last_exe_1c():
    result = None

    estart_file_path = Path(site_data_dir('1CEStart', '1C')) / '1CEStart.cfg'
    installed_location_paths = []
    if estart_file_path.is_file():
        with estart_file_path.open(encoding='utf-16') as estart_file:
            for line in estart_file.readlines():
                key_and_value = line.split('=')
                if key_and_value[0] == 'InstalledLocation':
                    value = '='.join(key_and_value[1:])
                    installed_location_paths.append(Path(value.rstrip()))

        platform_versions = []
        for installed_location_path in installed_location_paths:
            if installed_location_path.is_dir():
                for p1 in installed_location_path.iterdir():
                    version_as_number = get_version_as_number(str(p1.name))
                    if version_as_number != 0:
                        p2 = p1 / 'bin' / '1cv8.exe'
                        if p2.is_file():
                            platform_versions.append((version_as_number, p2))

        platform_versions_reversed = sorted(platform_versions, key=lambda x: x[0], reverse=True)
        if platform_versions_reversed:
            result = platform_versions_reversed[0][1]
    else:
        raise SettingsError('1CEStart.cfg file does not exist!')

    return result


class Error(Exception):
    def __init__(self, value=None):
        super(Error, self).__init__()
        self.value = value

    def __str__(self):
        return repr(self.value)


class SettingsError(Error):
    def __init__(self, message: str):
        super().__init__('{}'.format(message))
