import json
from typing import Any

import pytest

from application import Application, InvalidFilenameError, InvalidOrderError


def _read_json(filepath: str) -> Any:
    with open(filepath) as f:
        return json.load(f)


_SORTED_BY_ASC = {
    'user1': {
        'age': 35,
        'name': 'Wade Williams',
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
    'user2': {
        'age': 45,
        'gender': 'Male',
        'name': 'Wade Williams',
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
        'age': 30,
        'gender': 'Female',
        'name': 'Daisy Harris',
        'occupation': 'High School Teacher',
        'skills': {
            'languages': [
                'English',
                'Spanish'],
            'expertise': ['Teaching Foreign Language'],
        },
    },
}

_SORTED_BY_DESC = {
    'user3': {
        'skills': {
            'languages': [
                'English',
                'Spanish'],
            'expertise': ['Teaching Foreign Language'],
        },
        'occupation': 'High School Teacher',
        'name': 'Daisy Harris',
                'gender': 'Female',
                'age': 30,
    },
    'user2': {
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
        'occupation': 'Global Trading Marketer',
        'name': 'Wade Williams',
        'gender': 'Male',
        'age': 45,
    },
    'user1': {
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
        'occupation': 'Software Engineer',
        'name': 'Wade Williams',
        'age': 35,
    },
}


def test_sort_json_data_by_asc(users_workspace: tuple[str, str, str]) -> None:
    dirname, filename, filepath = users_workspace
    Application(dirname=dirname, filename=filename).run()
    assert _read_json(filepath) == _SORTED_BY_ASC


def test_sort_json_data_by_desc(users_workspace: tuple[str, str, str]) -> None:
    dirname, filename, filepath = users_workspace
    Application(dirname=dirname, filename=filename, order='desc').run()
    assert _read_json(filepath) == _SORTED_BY_DESC


def test_sort_json_data_with_missing_filename(
        users_workspace: tuple[str, str, str]) -> None:
    dirname, _, _ = users_workspace
    with pytest.raises(InvalidFilenameError, match=r'^Filename must be provided\.$'):
        Application(dirname=dirname, filename='').run()


def test_sort_json_data_with_invalid_order(
        users_workspace: tuple[str, str, str]) -> None:
    dirname, filename, _ = users_workspace
    with pytest.raises(InvalidOrderError, match=r'^Order option must be either asc or desc\.$'):
        Application(dirname=dirname, filename=filename, order='hoge').run()


def test_sort_json_data_with_non_string_order(
        users_workspace: tuple[str, str, str]) -> None:
    dirname, filename, _ = users_workspace
    with pytest.raises(InvalidOrderError, match=r'^Unexpected param was provided$'):
        Application(dirname=dirname, filename=filename,
                    order=1).run()  # type: ignore[arg-type]
