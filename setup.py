from setuptools import setup
from setuptools import find_packages


setup(
    name='django-aliyun-oss-backend-storage',
    version='0.1',
    packages=find_packages(),
    author='Ph87'
    author_email='issue.of+django_aliyun_oss_backend_storage'
    url='https://github.com/ph87/django-aliyun-oss-backend-storage/',
    description='Django Aliyun OSS backend storage, integrated with Aliyun SDK 0.4.6',
    long_description=open('README.md').read(),
    license='MIT License',
    requires=[
        'Django',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: System :: Installation/Setup'
    ],
    include_package_data=True,
    zip_safe=False
)
