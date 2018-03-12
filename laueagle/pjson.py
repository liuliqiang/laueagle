from __future__ import print_function

import  json

import click


@click.command('Json linter')
@click.option(
    '-f',
    '--file',
    type=str,
    required=True,
    help='file for lint',
)
def json_lint(file):
    print("todo feature")


@click.command('Json formater')
@click.option('-f', '--filepath', type=str, required=True,help='Json file path for format',)
@click.option('-r', '--replace', type=bool, required=False, default=True, help='Output formatted file replace old',)
@click.option('-n', '--newfile', type=str, required=False, default='./formatted.json', help='Formatted new file',)
def json_format(filepath, replace, newfile):
    with open(filepath) as f:
        data = json.load(f)

    if replace:
        outfilepath = filepath
    else:
        outfilepath = newfile
    with open(outfilepath, "w") as wf:
        json.dump(data, wf, indent=4)
