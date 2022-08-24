from setuptools import setup, find_packages
setup(
    name = 'test-pipeline',
    version = '1.0',
    packages = find_packages(include = ('testpipeline*', )),
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.3.1'],
    entry_points = {
'console_scripts' : [
'main = testpipeline.pipeline:main', ], },
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
