Feature: testing browser title
 
Scenario Outline: visit <browser page> and check
    When we visit <browser page>
    Then it should have a title "<browser title>"
    Then there should be a search bar
 
Examples: Browser
    | browser page                     | browser title |
    | https://crash-stats.mozilla.com/ | Crash Data for Firefox |