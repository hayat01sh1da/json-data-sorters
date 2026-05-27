import inspect
import json
import os
from typing import Any


class Application:
    """Reads a JSON object file, sorts its top-level keys (and any nested
    dict/list values) ascending or descending, and rewrites it as pretty
    JSON."""

    class InvalidFilenameError(Exception):
        pass

    class InvalidOrderError(Exception):
        pass

    @classmethod
    def run(cls, dirname: str = '', filename: str = '',
            order: Any = 'asc') -> None:
        instance = cls(dirname=dirname, filename=filename, order=order)
        instance.validate_filename()
        instance.validate_order()
        instance._run()

    def __init__(self, dirname: str = '', filename: str = '',
                 order: Any = 'asc') -> None:
        self._dirname = dirname
        self._filename = filename
        self._filepath = os.path.join(dirname, filename)
        self._order = order

    def validate_filename(self) -> str:
        if not self._filename:
            raise self.InvalidFilenameError('Filename must be provided.')
        return self._filename

    def validate_order(self) -> str:
        if not isinstance(self._order, str) or \
                self._order not in ('asc', 'desc'):
            raise self.InvalidOrderError(
                'Order option must be either asc or desc.')
        return self._order

    # private

    def _run(self) -> None:
        self._output(f'Start exporting JSON data in {self._filepath}')
        os.makedirs(self._dirname, exist_ok=True)
        if not os.path.isfile(self._filepath):
            with open(self._filepath, 'w') as f:
                f.write('')
        dumped = self._dump_converted_json_data_with_sorting()
        with open(self._filepath, 'w') as f:
            f.write(dumped)
        self._output(f'Done export JSON data in {self._filepath} 🎉')

    def _json_data(self) -> dict[str, Any]:
        with open(self._filepath) as f:
            return json.load(f)

    def _converted_json_data_with_sorting(self) -> dict[str, Any]:
        return dict(sorted(
            self._json_data().items(),
            reverse=(self._order == 'desc'),
        ))

    def _dump_converted_json_data_with_sorting(self) -> str:
        sorted_hash = {
            key: self._sort_value(value)
            for key, value in
            self._converted_json_data_with_sorting().items()
        }
        return json.dumps(sorted_hash, ensure_ascii=False, indent=2)

    def _sort_value(self, value: Any) -> Any:
        if isinstance(value, dict):
            return dict(sorted(
                value.items(), reverse=(self._order == 'desc')))
        if isinstance(value, list):
            return sorted(value, reverse=(self._order == 'desc'))
        return value

    def _test_env(self) -> bool:
        stack = inspect.stack()
        if not stack:
            return False
        return 'pytest' in os.path.basename(stack[-1].filename)

    def _output(self, message: str) -> None:
        if not self._test_env():
            print(message)
