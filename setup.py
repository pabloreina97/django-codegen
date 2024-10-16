from setuptools import setup, find_packages

setup(
    name="django-codegen",
    version="0.1",
    packages=find_packages(),
    install_requires=["openai", "click"],
    entry_points={
        'console_scripts': [
            'django-codegen = django_codegen.cli.main:run',
        ],
    },
)
