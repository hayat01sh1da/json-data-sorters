import json

class Application:
  def __init__(self, filepath, order = 'asc'):
      self.filepath = filepath
      if order != 'asc' and order != 'desc':
          raise ValueError('order option must be either asc or desc')
      self.order = order

  def run(self):
      with open(self.filepath, 'a') as f:
          f.write(self.__dump_sorted_json_data__())

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
