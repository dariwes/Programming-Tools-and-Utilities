from setuptools import setup, find_packages

setup(
    name='serializer',
    version='1.0',
    author="Darya Shchedrova",
    author_email="shchedrovva@mail.ru",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'serializer = console_app:main',
        ],
    }
)