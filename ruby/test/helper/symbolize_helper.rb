# rbs_inline: enabled

module SymbolizeHelper
  # @rbs h: Hash[untyped, untyped]
  # @rbs return: Hash[untyped, untyped]
  def self.symbolize_recursive(hash, hsh = {})
    hsh.tap do |h|
      hash.each { |key, value| h[key.to_sym] = transform(value) }
    end
  end

  private

  # @rbs return: untyped
  def self.transform(object)
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
    # @rbs return: Hash[Symbol, untyped]
    def deep_symbolize_keys
      SymbolizeHelper.symbolize_recursive(self)
    end
  end
end
