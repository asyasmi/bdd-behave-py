Feature: Checking search on some page
    Scenario Outline: Сheck some text in search results
      Given user on '<page>' page
      Then input text '<term>' and click search
      Then page include text '<result>'

    Examples: ASCII text
        | page          | term          | result      |
        | home          | linux         | linux       |
        | links         | check         | check       |

    Examples: Cyrillic text
        | page          | term          | result      |
        | home          | линукс        | линукс      |
        | links         | проверка      | проверка    |
