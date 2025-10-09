require 'json'
require 'fileutils'

class Application
  def self.run(dirname:, filename:, order: :asc)
    order    = order.respond_to?(:to_sym) ? order.to_sym : order
    instance = new(dirname, filename, order)
    instance.validate_filename!
    instance.validate_order!
    instance.run
  end

  def initialize(dirname, filename, order)
    @dirname  = dirname
    @filename = filename
    @filepath = File.join(dirname, filename)
    @order    = order
  end

  def validate_filename!
    if filename.empty?
      raise 'Filename must be provided.'
    else
      filename
    end
  end

  def validate_order!
    case order
    when :asc, :desc
      order
    else
      raise 'Order option must be either :asc or :desc'
    end
  end

  def run
    FileUtils.mkdir(dirname) unless Dir.exist?(dirname)
    FileUtils.touch(filepath) unless File.exist?(filepath)
    File.write(filepath, dump_sorted_json_data)
  end

  private

  attr_reader :dirname, :filename, :filepath, :order

  def json_data
    File.open(filepath) { |f| JSON.load(f) }
  end

  def sorted_json_data
    return unless json_data
    order == :asc ? json_data.sort.to_h : json_data.sort.reverse.to_h
  end

  def dump_sorted_json_data
    return unless sorted_json_data
    sorted_json_data.each_with_object({}) { |(key, value), hash|
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
end
