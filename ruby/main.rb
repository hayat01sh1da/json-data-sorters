require_relative './src/application'

puts 'Provide the directory name you put the JSON file in:'
dirname = gets.chomp

puts 'Provide the filename of which JSON data name you would like to sort:'
filename = gets.chomp

puts 'Provide asc(default) or desc you would like to sort key-value in:'
order = gets.chomp

params = { dirname:, filename:, order: }.reject { |_, value| value.empty? }

Application.run(**params)
