from __future__ import print_function

import click


@click.command('Json linter')
# @click.option(
#     '-n',
#     '--name',
#     type=str,
#     required=True,
#     help='A name to greet you with',
# )
def json_lint():
    pass


@click.command('Json formater')
def json_format():
    pass
