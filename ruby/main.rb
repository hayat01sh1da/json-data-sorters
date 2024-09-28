require_relative './src/application'

puts 'Provide the directory name you put the JSON file in'
dirname = gets.chomp

puts 'Provide the filename of which JSON data name you would like to sort'
filename = gets.chomp

puts 'Provide asc(default) or desc you would like to sort key-value in'
order = gets.chomp

filepath = File.join(dirname, filename)

puts "Start exporting JSON data in #{filepath}"
application  = ::JsonDataSorter::Application.run(dirname:, filename:, order:)
puts "Done export JSON data in #{filepath} 🎉"
