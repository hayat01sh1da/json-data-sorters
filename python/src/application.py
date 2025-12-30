import os
import json

class Application:
    def __init__(self, dirname, filename, order = 'asc'):
        self.dirname = dirname
        if len(filename) == 0:
            raise ValueError('Filename must be provided.')
        self.filename = filename
        self.filepath = os.path.join(dirname, filename)
        if not str(type(order)) == "<class 'str'>":
            raise ValueError('Unexpected param was provided')
        if not (order == 'asc' or order == 'desc'):
            raise ValueError('Order option must be either asc or desc.')
        self.order = order
        self.env   = inspect.stack()[1].filename.split('/')[-2]

    def run(self):
        self.__output__('Start exporting JSON data in {filepath}'.format(filepath = self.filepath))
        os.makedirs(self.dirname, exist_ok = True)
        if not os.path.isfile(self.filepath):
            with open(self.filepath, 'w') as f:
                f.write('')
        try:
            with open(self.filepath, 'a') as f:
                f.write(self.__dump_sorted_json_data__())
        except json.decoder.JSONDecodeError:
            with open(self.filepath, 'a') as f:
                f.write('')
        self.__output__('Done exporting JSON data in {filepath} 🎉'.format(filepath = self.filepath))

    # private

    def __json_data__(self):
        json_data = None
        with open(self.filepath, 'r+') as f:
            json_data = json.load(f)
            f.truncate(0)
        return json_data

    def __sorted_json_data__(self):
        return dict(sorted(self.__json_data__().items())) if self.order == 'asc' else dict(sorted(self.__json_data__().items(), reverse = True))

    def __dump_sorted_json_data__(self):
        dictionary = {}
        for key, value in self.__sorted_json_data__().items():
            if isinstance(value, dict):
                dictionary[key] = dict(sorted(value.items())) if self.order == 'asc' else dict(sorted(value.items(), reverse = True))
            elif isinstance(value, list):
                dictionary[key] = sorted(value) if self.order == 'asc' else sorted(value, reverse = True)
            else:
                dictionary[key] = value
        return json.dumps(dictionary, ensure_ascii = False, indent = 2)

    def __is_test_env__(self):
        """Check if running in a test environment.
        
        Returns:
            bool: True if in test environment, False otherwise.
        """
        return self.env == 'test'

    def __output__(self, message):
        """Output a message if not running in the test environment.

        Args:
            message: The message to output.

        Returns:
            None
        """
        if not self.__is_test_env__():
            print(message)
