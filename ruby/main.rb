require_relative './src/application'

dirname      = File.join('..', 'json')
filename, *_ = ARGV
filename     = filename || ''
filepath     = File.join(dirname, filename)

puts "Start exporting JSON data in #{filepath}"
application  = ::JsonDataSorter::Application.run(dirname:, filename:)
puts "Done export JSON data in #{filepath} 🎉"
