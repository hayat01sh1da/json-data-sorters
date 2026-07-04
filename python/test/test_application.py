"""Tests the JSON data sorter against fixture data under test/fixtures/."""

import json
import os
from typing import Any

import pytest

from application import Application

_FIXTURES_DIR = os.path.join('.', 'test', 'fixtures')


def _read_json(filepath: str) -> Any:
    with open(filepath, encoding='utf-8') as f:
        return json.load(f)


def _fixture_json(basename: str) -> Any:
    return _read_json(os.path.join(_FIXTURES_DIR, basename))


def test_sort_json_data_by_asc(
        users_workspace: tuple[str, str, str]) -> None:
    dirname, filename, filepath = users_workspace
    Application.run(dirname=dirname, filename=filename, order='asc')
    assert _read_json(filepath) == _fixture_json('users_sorted_asc.json')


def test_sort_json_data_by_desc(
        users_workspace: tuple[str, str, str]) -> None:
    dirname, filename, filepath = users_workspace
    Application.run(dirname=dirname, filename=filename, order='desc')
    assert _read_json(filepath) == _fixture_json('users_sorted_desc.json')


def test_sort_json_data_with_no_filename(
        users_workspace: tuple[str, str, str]) -> None:
    dirname, _, _ = users_workspace
    with pytest.raises(
            Application.InvalidFilenameError,
            match=r'^Filename must be provided\.$'):
        Application.run(dirname=dirname, filename='')


def test_sort_json_data_with_invalid_order_type(
        users_workspace: tuple[str, str, str]) -> None:
    dirname, filename, _ = users_workspace
    with pytest.raises(
            Application.InvalidOrderError,
            match=r'^Order option must be either asc or desc\.$'):
        Application.run(dirname=dirname, filename=filename, order='hoge')


def test_sort_json_data_with_invalid_data_type_of_order(
        users_workspace: tuple[str, str, str]) -> None:
    dirname, filename, _ = users_workspace
    with pytest.raises(
            Application.InvalidOrderError,
            match=r'^Order option must be either asc or desc\.$'):
        Application.run(
            dirname=dirname, filename=filename, order=1)
