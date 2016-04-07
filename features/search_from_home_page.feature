Feature: Checking search
Scenario: Сheck some text in search results
  Given user on 'home' page
  Then input text 'linux' and click search
  Then page include text 'linux'
