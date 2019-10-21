Feature: Check about page
Scenario: Сheck some text on 'About' page
  Given user on 'home' page
  Then user see a text 'Built for developers'
  Then user clicks on link with text 'About'
  Then user see a text 'We’re supporting a community where more than 40 million'
