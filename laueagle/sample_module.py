from __future__ import print_function

import click


@click.command('A sample command')
@click.option(
    '-n',
    '--name',
    type=str,
    required=True,
    help='A name to greet you with',
)
def hello_world(name):
    print('Hello, {}!'.format(name))


@click.command('Yaml to json')
def yaml_to_json():
    pass


@click.command('Json to yaml')
def json_to_yaml():
    pass


if __name__ == '__main__':
    hello_world()
