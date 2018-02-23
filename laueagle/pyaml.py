import click

from yamllint import linter
from yamllint.config import YamlLintConfig


@click.command('Yaml linter')
@click.option(
    '-f',
    '--filepath',
    type=str,
    required=True,
    help='Yaml file path for lint',
)
def yaml_lint(filepath):
    conf = YamlLintConfig('extends: default')
    with open(filepath) as f:
        for p in linter.run(f, conf):
            print("Line: {} colume: {} {}".format(p.column, p.line, p.desc))


@click.command('Yaml formater')
def yaml_format():
    pass

