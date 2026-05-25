# frozen_string_literal: true
# rbs_inline: enabled

require 'json'

class Application
  class InvalidFilenameError < StandardError; end
  class InvalidOrderError < StandardError; end

  # @rbs dirname: String
  # @rbs filename: String
  # @rbs order: untyped
  # @rbs return: void
  def self.run(dirname: '', filename: '', order: :asc)
    order    = order.to_sym if order.respond_to?(:to_sym)
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
    raise InvalidFilenameError, 'Filename must be provided.' if filename.empty?

    filename
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
    FileUtils.mkdir_p(dirname)
    FileUtils.touch(filepath) unless File.exist?(filepath)
    File.write(filepath, dump_converted_json_data_with_sorting)
    output "Done export JSON data in #{filepath} 🎉"
  end

  private

  attr_reader :dirname, :filename, :filepath, :order

  # @rbs return: Hash[String, untyped]?
  def json_data
    File.open(filepath) { |f| JSON.parse(f) }
  end

  # @rbs return: Hash[String, untyped]?
  def converted_json_data_with_sorting
    sorted_json_data = json_data&.sort
    order == :asc ? sorted_json_data&.to_h : sorted_json_data&.reverse&.to_h
  end

  # @rbs hash: Hash[String, untyped]
  # @rbs return: String
  def dump_converted_json_data_with_sorting(hash = {})
    sorted_hash = converted_json_data_with_sorting&.each_with_object(hash) do |(key, value), acc|
      acc[key] = sort_value(value)
    end
    JSON.pretty_generate(sorted_hash)
  end

  # @rbs value: untyped
  # @rbs return: untyped
  def sort_value(value)
    case value
    when Hash
      order == :asc ? value.sort.to_h : value.sort.reverse.to_h
    when Array
      order == :asc ? value.sort : value.sort.reverse
    else
      value
    end
  end

  # @rbs return: bool
  def test_env?
    caller(0..0).first.split('/').last.include?('minitest.rb')
  end

  # @rbs message: String
  # @rbs return: void
  def output(message)
    puts message unless test_env?
  end
end
