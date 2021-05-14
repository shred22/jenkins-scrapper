#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
# the python unittest plugin allows running python's standard library unittests
use_plugin("python.unittest")
# this plugin allows installing project dependencies with pip
use_plugin("python.install_dependencies")
# a linter plugin that runs flake8 (pyflakes + pep8) on our project sources
use_plugin("python.flake8")
# a plugin that measures unit test statement coverage
use_plugin("python.coverage")
# for packaging purposes since we'll build a tarball
use_plugin("python.distutils")



name = "jenkins-scrapper"
default_task = "publish"


@init
def set_properties(project):
    project.version = "0.1.14"
    project.depends_on_requirements("requirements.txt")


