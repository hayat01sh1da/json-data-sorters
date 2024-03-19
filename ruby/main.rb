require_relative './src/application'

filepath    = File.join('json', 'settings.json')
application = ::JsonDataSorter::Application.run(filepath:)
puts "JSON data has been successfully exported in #{filepath} 🎉"
