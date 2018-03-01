# -*- coding: utf-8 -*-

"""
    Author: liqianglau@outlook.com
    Created at: 2018-03-02 00:36
    Update: -

    Copyright (c) 2013-2018, SMARTX
    All rights reserved.
"""
import os

import click
import yaml

from yamllint import linter
from yamllint.config import YamlLintConfig


def _yaml_lint(filepath):
    conf = YamlLintConfig('extends: default')

    has_error = False
    with open(filepath) as f:
        for p in linter.run(f, conf):
            if p.level == "error":
                has_error = True
                print("Line: {} column: {} {}".format(
                        p.line, p.column, p.desc))

    return not has_error


@click.command('Yaml linter')
@click.option(
    '-f',
    '--filepath',
    type=str,
    required=True,
    help='Yaml file path for lint',
)
def yaml_lint(filepath):
    if _yaml_lint(filepath):
        _, filename = os.path.split(filepath)
        print("Congratulation! {} in good format now!".format(filename))


@click.command('Yaml formater')
@click.option('-f', '--filepath', type=str, required=True,help='Yaml file path for lint',)
@click.option('-r', '--replace', type=bool, required=False, default=True, help='Output formatted file replace old',)
@click.option('-n', '--newfile', type=str, required=False, default='./formatted.yml', help='Formatted new file',)
def yaml_format(filepath, replace, newfile):
    status = _yaml_lint(filepath)
    if status:
        with open(filepath) as f:
            yaml_cont = f.read()
        yaml_dict = yaml.load(yaml_cont)
        outfilepath = newfile
        if replace:
            outfilepath = filepath
        with open(outfilepath, "w") as wf:
            yaml.dump(yaml_dict, wf, default_flow_style=False)
    else:
        print("Fix the error first!")
