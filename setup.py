import os
from distutils.command.build import build

from django.core import management
from setuptools import setup, find_packages


try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''


class CustomBuild(build):
    def run(self):
        management.call_command('compilemessages', verbosity=1, interactive=False)
        build.run(self)


cmdclass = {
    'build': CustomBuild
}


setup(
    name='pretix-siteimprove',
    version='1.0.0',
    description='Adds Siteimprove to Pretix',
    long_description=long_description,
    url='https://github.com/rimi-itk/pretix-siteimprove.git',
    author='Mikkel Ricky',
    author_email='rimi@aarhus.dk',
    license='Apache Software License',

    install_requires=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretix.plugin]
pretix_siteimprove=pretix_siteimprove:PretixPluginMeta
""",
)
