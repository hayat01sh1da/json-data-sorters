import pytest
import re
import os
import shutil
import sys
from collections.abc import Iterator

sys.path.append('./src')

_FIXTURES_DIR = os.path.join('.', 'test', 'fixtures')


@pytest.fixture(autouse=True)
def __cleanup_caches__() -> Iterator[None]:
    yield
    cache_dir = re.compile(r'^(?:__pycache__|\.pytest_cache|\.mypy_cache)$')
    for root, dirs, _ in os.walk('.'):
        for name in list(dirs):
            if cache_dir.match(name):
                shutil.rmtree(os.path.join(root, name), ignore_errors=True)
                dirs.remove(name)


@pytest.fixture
def users_workspace() -> Iterator[tuple[str, str, str]]:
    dirname = os.path.join('.', 'test', 'tmp')
    filename = 'users.json'
    filepath = os.path.join(dirname, filename)
    os.makedirs(dirname, exist_ok=True)
    shutil.copyfile(os.path.join(_FIXTURES_DIR, filename), filepath)
    yield dirname, filename, filepath
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
