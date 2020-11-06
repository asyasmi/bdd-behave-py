# Created by asmi at 06.11.2020
Feature: Check status page
Scenario: Check some text on 'Status' page
  Given user on 'home' page
  Then set cookie 'cookie-preferences' to 'analytics:accepted'
  Then user clicks on link with text 'Status'
  Then user is redirected to page 'status_page'
