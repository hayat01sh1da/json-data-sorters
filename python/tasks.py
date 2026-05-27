import os
import sys

from invoke import Context, task

_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_ROOT, 'src'))

from application import Application  # noqa: E402


@task
def run_json_data_sorter(c: Context) -> None:
    """Run JSON Data Sorter"""
    print('Provide the directory name you put the JSON file in')
    dirname = input().strip()

    print('Provide the filename of which JSON data name you would like '
          'to sort')
    filename = input().strip()

    print('Provide asc(default) or desc you would like to sort '
          'key-value in')
    order = input().strip()

    params: dict[str, str] = {}
    for key, value in {
        'dirname': dirname, 'filename': filename, 'order': order,
    }.items():
        if value:
            params[key] = value

    Application.run(**params)


@task(default=True)
def test(c: Context) -> None:
    """Run all tests"""
    c.run('pytest .')
