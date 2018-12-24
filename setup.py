import os

from setuptools import setup


def file_path(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(file_path(fname)).read()


def desc():
    info = read('README.rst')
    try:
        return info + '\n\n' + read('changelog.rst')
    except IOError:
        return info


setup(
    name='flask-admin-toggle-control',
    version='0.1.0',
    packages=['src/flask_admin_toggle_control'],
    url='https://github.com/artemShelest/flask-admin-toggle-control',
    license='MIT',
    author='Artem Shelest',
    author_email='artem.e.shelest@gmail.com',
    description='Toggle control for Flask Admin inline form.',
    long_description=desc(),
    keywords=['flask-admin', 'inline', 'form', 'control', 'bool', 'boolean', 'toggle'],
    install_requires=[
        'flask-admin',
        'wtforms',
        'jinja2'
    ],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
