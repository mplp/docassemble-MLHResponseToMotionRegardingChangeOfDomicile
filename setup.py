import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.MLHResponseToMotionRegardingChangeOfDomicile',
      version='1.0.5',
      description=('A Response to a Motion Regarding Change of Domicile for use in Michigan Family Courts'),
      long_description='# docassemble.MLHResponseToMotionRegardingChangeOfDomicile\r\n\r\nA response to a motion regarding change of domicile in Michigan\r\n\r\n## Author\r\n- Pratibha Bharti\r\n- Emily Kress Miller\r\n- Rami Lorca\r\n\r\n## Changelog\r\n* 2/13/25  1.0.5 Behind-the-scenes court logic adjustment\r\n* 9/30/24  1.0.4 update user survey\r\n* 9/25/24  1.0.3 fix instructions header issue\r\n* 9/25/24  1.0.2 Fix italics issue\r\n* 9/25/24  1.0.1 edit subtitle and description\r\n* 9/20/24  1.0.0 Preparing to launch',
      long_description_content_type='text/markdown',
      author='Michigan Poverty Law Program',
      author_email='michiganlegalhelp@mplp.org',
      license='MIT License',
      url='https://michiganlegalhelp.org/resources/family/do-it-yourself-motion-change-domicile-response',
      packages=find_namespace_packages(),
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/MLHResponseToMotionRegardingChangeOfDomicile/', package='docassemble.MLHResponseToMotionRegardingChangeOfDomicile'),
     )

