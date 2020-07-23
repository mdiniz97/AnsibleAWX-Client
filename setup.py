from setuptools import  setup, find_packages

setup(
    name="ansibleawx-client",
    version="0.1.0",
    description="Ansible AWX Client",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
    ],
)