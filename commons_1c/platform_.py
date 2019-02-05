# -*- coding: utf-8 -*-
import os
from pathlib import Path

from appdirs import site_data_dir

from commons_1c.version import get_version_as_number


def get_last_1c_exe_file_fullpath(**kwargs) -> Path:
    result = None
    if 'config_file_path' in kwargs:
        # todo Может быть относительный путь
        config_file_fullpath = Path(kwargs['config_file_path'])
    else:
        config_file_fullpath = Path(site_data_dir('1CEStart', '1C'), '1CEStart.cfg')
    if config_file_fullpath.is_file():
        installed_location_fullpaths = []
        with config_file_fullpath.open(encoding='utf-16') as config_file:
            for line in config_file.readlines():
                key_and_value = line.split('=')
                if key_and_value[0] == 'InstalledLocation':
                    value = '='.join(key_and_value[1:])
                    installed_location_fullpaths.append(Path(value.rstrip('\r\n')))
        platform_versions = []
        for installed_location_fullpath in installed_location_fullpaths:
            if installed_location_fullpath.is_dir():
                for version_dir_shortname in os.listdir(installed_location_fullpath):  # todo
                    version_dir_fullpath = Path(installed_location_fullpath, version_dir_shortname)
                    version_as_number = get_version_as_number(version_dir_shortname)
                    if version_as_number:
                        exe_file_fullpath = Path(version_dir_fullpath, 'bin', '1cv8.exe')
                        if exe_file_fullpath.is_file():
                            platform_versions.append((version_as_number, exe_file_fullpath))
        platform_versions_reversed = sorted(platform_versions, key=lambda x: x[0], reverse=True)
        if platform_versions_reversed:
            result = platform_versions_reversed[0][1]
    else:
        raise FileExistsError('1CEStart.cfg file does not exist')
    return result
