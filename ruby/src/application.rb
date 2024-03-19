require 'json'

module JsonDataSorter
  class Application
    def self.run(filepath:, order: :asc)
      self.new(filepath, validate!(order)).run
    end

    def initialize(filepath, order)
      @filepath = filepath
      @order    = order
    end

    def run
      IO.write(filepath, dump_sorted_json_data)
    end

    private

    attr_reader :filepath, :order

    class << self
      def validate!(order)
        order = order.to_sym
        case order
        when :asc, :desc
          order
        else
          raise 'Order option must be either :asc or :desc'
        end
      end
    end

    def json_data
      File.open(filepath) { |f| JSON.load(f) }
    end

    def sorted_json_data
      order == :asc ? json_data.sort.to_h : json_data.sort.reverse.to_h
    end

    def dump_sorted_json_data
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
end
