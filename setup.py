from setuptools import setup

setup(
    name="coffee",
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        coffee=coffee:coffee
    ''',
)