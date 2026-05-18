import pytest
import re
import json
import os
import shutil
import sys
from collections.abc import Iterator

sys.path.append('./src')


_USER_DATA = {
    'user2': {
        'name': 'Wade Williams',
        'age': 45,
        'gender': 'Male',
        'occupation': 'Global Trading Marketer',
        'skills': {
            'languages': [
                'Japanese',
                'English',
                'Spanish',
                'German',
                'French'],
            'expertise': [
                'Marketing',
                'Accounting',
                'Interpretation',
                'Translation',
                'Economics'],
        },
    },
    'user3': {
        'name': 'Daisy Harris',
        'age': 30,
        'gender': 'Female',
        'occupation': 'High School Teacher',
        'skills': {
            'languages': [
                'English',
                'Spanish'],
            'expertise': ['Teaching Foreign Language'],
        },
    },
    'user1': {
        'name': 'Wade Williams',
        'age': 35,
        'occupation': 'Software Engineer',
        'skills': {
            'languages': [
                'Japanese',
                'English'],
            'expertise': [
                'Server-Side Programming',
                'Front-end Programming',
                'Infrastructure Management',
                'Team Members Management',
            ],
        },
    },
}


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
    with open(filepath, 'w') as f:
        f.write(json.dumps(_USER_DATA, ensure_ascii=False, indent=2))
    yield dirname, filename, filepath
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
