require 'minitest/autorun'
require 'json'
require 'active_support/core_ext/hash/keys'
require_relative '../src/application'

class ApplicationTest < Minitest::Test
  def setup
    @dirname  = File.join('.', 'test', 'tmp')
    @filename = 'users.json'
    @filepath = File.join(dirname, filename)
    FileUtils.mkdir_p(dirname) unless Dir.exist?(dirname)
    File.write(filepath, json_data)
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
    error = assert_raises RuntimeError do
      Application.run(dirname:, filename: '')
    end
    assert_equal('Filename must be provided.', error.message)
  end

  def test_sort_json_data_with_invalid_order_type
    error = assert_raises RuntimeError do
      Application.run(dirname:, filename:, order: :hoge)
    end
    assert_equal('Order option must be either :asc or :desc', error.message)
  end

  def test_sort_json_data_with_invalid_data_type_of_order
    error = assert_raises RuntimeError do
      Application.run(dirname:, filename:, order: 1)
    end
    assert_equal('Order option must be either :asc or :desc', error.message)
  end

  private

  attr_reader :dirname, :filename, :filepath

  def actual_json
    File.open(filepath) { |f| JSON.load(f).deep_symbolize_keys }
  end

  def json_data
    JSON.dump(user_data)
  end

  # Conf. https://7esl.com/english-names/
  def user_data
    {
      user2: {
        name: 'Wade Williams',
        age: 45,
        gender: 'Male',
        occupation: 'Global Trading Marketer',
        skills: {
          languages: [
            'Japanese',
            'English',
            'Spanish',
            'German',
            'French'
          ],
          expertise: [
            'Marketing',
            'Accounting',
            'Interpretation',
            'Translation',
            'Economics'
          ]
        }
      },
      user3: {
        name: 'Daisy Harris',
        age: 30,
        gender: 'Female',
        occupation: 'High School Teacher',
        skills: {
          languages: [
            'English',
            'Spanish'
          ],
          expertise: [
            'Teaching Foreign Language'
          ]
        }
      },
      user1: {
        name: 'Wade Williams',
        age: 35,
        occupation: 'Software Engineer',
        skills: {
          languages: [
            'Japanese',
            'English'
          ],
          expertise: [
            'Server-Side Programming',
            'Front-end Programming',
            'Infrastructure Management',
            'Team Members Management',
          ]
        }
      }
    }
  end

  def sorted_user_data_by_asc
    {
      user1: {
        age: 35,
        name: 'Wade Williams',
        occupation: 'Software Engineer',
        skills: {
          languages: [
            'Japanese',
            'English'
          ],
          expertise: [
            'Server-Side Programming',
            'Front-end Programming',
            'Infrastructure Management',
            'Team Members Management'
          ]
        }
      },
      user2: {
        age: 45,
        gender: 'Male',
        name: 'Wade Williams',
        occupation: 'Global Trading Marketer',
        skills: {
          languages: [
            'Japanese',
            'English',
            'Spanish',
            'German',
            'French'
          ],
          expertise: [
            'Marketing',
            'Accounting',
            'Interpretation',
            'Translation',
            'Economics'
          ]
        }
      },
      user3: {
        age: 30,
        gender: 'Female',
        name: 'Daisy Harris',
        occupation: 'High School Teacher',
        skills: {
          languages: [
            'English',
            'Spanish'
          ],
          expertise: [
            'Teaching Foreign Language'
          ]
        }
      }
    }
  end

  def sorted_user_data_by_desc
    {
      user3: {
        skills: {
          languages: [
            'English',
            'Spanish'
          ],
          expertise: [
            'Teaching Foreign Language'
          ]
        },
        occupation: 'High School Teacher',
        name: 'Daisy Harris',
        gender: 'Female',
        age: 30
      },
      user2: {
        skills: {
          languages: [
            'Japanese',
            'English',
            'Spanish',
            'German',
            'French'
          ],
          expertise: [
            'Marketing',
            'Accounting',
            'Interpretation',
            'Translation',
            'Economics'
          ]
        },
        occupation: 'Global Trading Marketer',
        name: 'Wade Williams',
        gender: 'Male',
        age: 45
      },
      user1: {
        skills: {
          languages: [
            'Japanese',
            'English'
          ],
          expertise: [
            'Server-Side Programming',
            'Front-end Programming',
            'Infrastructure Management',
            'Team Members Management'
          ]
        },
        occupation: 'Software Engineer',
        name: 'Wade Williams',
        age: 35
      }
    }
  end
end
