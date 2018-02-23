from laueagle import sample_module
from click.testing import CliRunner


def test_hello_world():
    test_runner = CliRunner()
    response = test_runner.invoke(
        sample_module.hello_world, ['--name', 'Mitchell']
    )

    assert response.exit_code == 0
    assert response.output == 'Hello, Mitchell!\n'
