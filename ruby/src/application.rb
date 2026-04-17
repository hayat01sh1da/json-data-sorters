# rbs_inline: enabled

require 'json'
require 'fileutils'

class Application
  class InvalidFilenameError < StandardError; end
  class InvalidOrderError < StandardError; end

  # @rbs dirname: String
  # @rbs filename: String
  # @rbs order: untyped
  # @rbs return: void
  def self.run(dirname: '', filename: '', order: :asc)
    order    = order.respond_to?(:to_sym) ? order.to_sym : order
    instance = new(dirname:, filename:, order:)
    instance.validate_filename!
    instance.validate_order!
    instance.run
  end

  # @rbs dirname: String
  # @rbs filename: String
  # @rbs order: untyped
  # ⚠️ `order` expects a class which can be converted to Symbol by `to_sym` method(e.g. String, Symbol).
  # ⚠️ Otherwise, it will raise an error when validating order.
  # @rbs return: void
  def initialize(dirname: '', filename: '', order: :asc)
    @dirname  = dirname
    @filename = filename
    @filepath = File.join(dirname, filename)
    @order    = order
  end

  # @rbs return: String
  def validate_filename!
    if filename.empty?
      raise InvalidFilenameError, 'Filename must be provided.'
    else
      filename
    end
  end

  # @rbs return: Symbol
  def validate_order!
    case order
    when :asc, :desc
      order
    else
      raise InvalidOrderError, 'Order option must be either :asc or :desc'
    end
  end

  # @rbs return: void
  def run
    output "Start exporting JSON data in #{filepath}"
    FileUtils.mkdir(dirname) unless Dir.exist?(dirname)
    FileUtils.touch(filepath) unless File.exist?(filepath)
    File.write(filepath, dump_sorted_json_data)
    output "Done export JSON data in #{filepath} 🎉"
  end

  private

  attr_reader :dirname, :filename, :filepath, :order

  # @rbs return: Hash[String, untyped]?
  def json_data
    File.open(filepath) { |f| JSON.load(f) }
  end

  # @rbs return: Hash[String, untyped]?
  def sorted_json_data
    order == :asc ? json_data&.sort&.to_h : json_data&.sort&.reverse&.to_h
  end

  # @rbs hash: Hash[String, untyped]
  # @rbs return: String
  def dump_sorted_json_data(hash = {})
    sorted_json_data&.each_with_object(hash) { |(key, value), hash|
      hash[key] = case value
      when Hash
        order == :asc ? value.sort.to_h : value.sort.reverse.to_h
      when Array
        order == :asc ? value.sort : value.sort.reverse
      else
        value
      end
    }.then { |sorted_hash|
      JSON.pretty_generate(sorted_hash)
    }
  end

  # @rbs return: bool
  def test_env?
    caller[-1].split('/').last.match?(/minitest\.rb/)
  end

  # @rbs message: String
  # @rbs return: void
  def output(message)
    puts message unless test_env?
  end
end
