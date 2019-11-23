""" 
Bite 166. Complete a tox ini file parser class
"""
import configparser
from os import path

DJANGO_TOX_FILE = path.join(path.dirname(__file__), 'tmp', 'django-tox.ini')
COOKIE_TOX_FILE = path.join(path.dirname(__file__), 'tmp','cookiecutter-tox.ini')
OEUVRE_TOX_FILE = path.join(path.dirname(__file__), 'tmp', 'oeuvre-tox.ini')
PYRAMID_TOX_FILE = path.join(path.dirname(__file__), 'tmp', 'pyramid-tox.ini')


class ToxIniParser:
    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)
        # print(self.config.sections())

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)
        """
        if 'tox' in self.config:

            if '\n' in self.config['tox']['envlist']:
                con = []
                for line in self.config['tox']['envlist'].strip().splitlines():
                    if ',' in line:
                        con += line.split(',')
                    else:
                        con.append(line)
                return sorted([v for v in con if v != ''])
            else:
                return sorted([
                    v.strip() for v in self.config['tox']['envlist'].split(",")
                ])

        return []

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        py_versions = set()
        for key in self.config.keys():
            if 'basepython' in self.config[key]:
                py_versions.add(self.config[key]['basepython'])

        return list(py_versions)


if __name__ == "__main__":
    tox_a = ToxIniParser(COOKIE_TOX_FILE)
    print(tox_a.number_of_sections)
    print(tox_a.environments)
    print(tox_a.base_python_versions)

    print("-" * 45)

    tox_b = ToxIniParser(DJANGO_TOX_FILE)
    print(tox_b.number_of_sections)
    print(tox_b.environments)
    print(tox_b.base_python_versions)

    print("-" * 45)

    tox_d = ToxIniParser(PYRAMID_TOX_FILE)
    print(tox_d.number_of_sections)
    print(tox_d.environments)
    print(tox_d.base_python_versions)

    print("-" * 45)

    tox_c = ToxIniParser(OEUVRE_TOX_FILE)
    print(tox_c.number_of_sections)
    print(tox_c.environments)
    print(tox_c.base_python_versions)
