# -*- coding: utf-8 -*-
from pathlib import Path
import re
from typing import List

from appdirs import site_data_dir

__version__ = '1.2.0'

pattern_version = re.compile(r'\D*(?P<version>(?:(\d+)|)(?:\.(\d+)|)(?:\.(\d+)|)(?:\.(\d+)|))\D*')


def get_version_as_number(version: str) -> int:
    result = 0

    m = 10000

    match = pattern_version.match(version)
    if match is not None:
        a = match.group(2)
        a = '0' if a is None else a

        b = match.group(3)
        b = '0' if b is None else b

        c = match.group(4)
        c = '0' if c is None else c

        d = match.group(5)
        d = '0' if d is None else d

        result = int(a) * m ** 3 + int(b) * m ** 2 + int(c) * m + int(d)

    return result


def get_version_as_parts(version: str) -> List[str]:
    result = []

    match = pattern_version.match(version)
    if match is not None:
        a = match.group(2)
        if a is not None:
            result.append(a)

        b = match.group(3)
        if b is not None:
            result.append(b)

        c = match.group(4)
        if c is not None:
            result.append(c)

        d = match.group(5)
        if d is not None:
            result.append(d)

    return result


def get_last_1c_exe_file_path(**kwargs) -> Path:
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
        raise Exception('1CEStart.cfg file does not exist!')

    return result
