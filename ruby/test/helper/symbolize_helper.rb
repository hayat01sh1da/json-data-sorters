module SymbolizeHelper
  extend self

  def symbolize_recursive(hash)
    {}.tap do |h|
      hash.each { |key, value| h[key.to_sym] = transform(value) }
    end
  end

  private

  def transform(object)
    case object
    when Hash
      symbolize_recursive(object)
    when Array
      object.map { |value| transform(value) }
    else
      object
    end
  end

  refine Hash do
    def deep_symbolize_keys
      SymbolizeHelper.symbolize_recursive(self)
    end
  end
end
