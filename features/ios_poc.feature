@android @ios
Feature: POC Login

    Scenario: Log into the iOS app and view invest account
        Given I am logged in
        When I navigate to the invest screen
        Then I can see my invest details