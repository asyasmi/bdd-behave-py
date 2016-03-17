Feature: Checking search
Scenario: Сheck some text in search results
  Given website 'linuxhub.ru'
  Then input text 'linux' and click search
  Then page include text 'linux'
