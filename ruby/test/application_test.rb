# frozen_string_literal: true
# rbs_inline: enabled

require 'minitest/autorun'
require 'json'
require_relative '../src/application'
require_relative 'helper/symbolize_helper'

# Tests the JSON data sorter against fixture data under test/fixtures/.
# Conf. https://7esl.com/english-names/ for the fixture names.
class ApplicationTest < Minitest::Test
  using SymbolizeHelper

  FIXTURES_DIR = File.join('.', 'test', 'fixtures') #: String

  def setup
    @dirname  = File.join('.', 'test', 'tmp')
    @filename = 'users.json'
    @filepath = File.join(dirname, filename)
    FileUtils.mkdir_p(dirname)
    FileUtils.cp(File.join(FIXTURES_DIR, 'users.json'), filepath)
  end

  def teardown
    FileUtils.rm_rf(dirname)
  end

  ########## Regular Cases ##########

  def test_sort_json_data_by_asc
    Application.run(dirname:, filename:, order: :asc)

    assert_equal(sorted_user_data_by_asc, actual_json)
  end

  def test_sort_json_data_by_desc
    Application.run(dirname:, filename:, order: :desc)

    assert_equal(sorted_user_data_by_desc, actual_json)
  end

  ########## Irregular Cases ##########

  def test_sort_json_data_with_no_filename
    error = assert_raises Application::InvalidFilenameError do
      Application.run(dirname:, filename: '')
    end
    assert_equal('Filename must be provided.', error.message)
  end

  def test_sort_json_data_with_invalid_order_type
    error = assert_raises Application::InvalidOrderError do
      Application.run(dirname:, filename:, order: :hoge)
    end
    assert_equal('Order option must be either :asc or :desc', error.message)
  end

  def test_sort_json_data_with_invalid_data_type_of_order
    error = assert_raises Application::InvalidOrderError do
      Application.run(dirname:, filename:, order: 1)
    end
    assert_equal('Order option must be either :asc or :desc', error.message)
  end

  private

  attr_reader :dirname, :filename, :filepath

  def actual_json
    File.open(filepath) { |f| JSON.parse(f.read).deep_symbolize_keys }
  end

  # @rbs basename: String
  # @rbs return: Hash[Symbol, untyped]
  def fixture_json(basename)
    File.open(File.join(FIXTURES_DIR, basename)) { |f| JSON.parse(f.read).deep_symbolize_keys }
  end

  def sorted_user_data_by_asc
    fixture_json('users_sorted_asc.json')
  end

  def sorted_user_data_by_desc
    fixture_json('users_sorted_desc.json')
  end
end
