import os
import json

class Application:
  def __init__(self, dirname, filename, order = 'asc'):
      self.dirname = dirname
      if len(filename) == 0:
          raise ValueError('Filename must be provided')
      self.filename = filename
      self.filepath = os.path.join(dirname, filename)
      if not (order == 'asc' or order == 'desc'):
          raise ValueError('Order option must be either asc or desc')
      if not str(type(order)) == "<class 'str'>":
          raise ValueError('Unexpected param was provided')
      self.order = order

  def run(self):
      if not os.path.exists(self.dirname):
          os.makedirs(self.dirname)
      if not os.path.isfile(self.filepath):
          with open(self.filepath, 'w') as f:
              f.write('')
      try:
          with open(self.filepath, 'a') as f:
              f.write(self.__dump_sorted_json_data__())
      except json.decoder.JSONDecodeError:
          with open(self.filepath, 'a') as f:
              f.write('')

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
