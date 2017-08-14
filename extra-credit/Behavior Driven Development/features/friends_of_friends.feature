Feature: Query friends of friends of a given person

    Scenario: Querying FoF of existing person with no friends results in an empty list of people
        Given a network
        And with Tom as a person
        And with Jan as a person
        And with Joe as a person
        And with Jan and Joe as friends
        When we query for friends of friends of Tom
        Then we get an empty list of people

    Scenario: Querying FoF of existing person with FoF results in a non-empty list of people who are friends of friends of the person
        Given a network
        And with Tom as a person
        And with Jan as a person
        And with Joe as a person
        And with Pam as a person
        And with Jan and Joe as friends
        And with Joe and Pam as friends
        When we query for friends of friends of Jan
        Then we get Jan and Pam as friends of friends

    Scenario: Querying FoF of existing person with FoF results in a non-empty list of people who are currently friends of friends of the person
        Given a network
        And with Tom as a person
        And with Jan as a person
        And with Joe as a person
        And with Pam as a person
        And with Jan and Joe as past friends
        And with Joe and Pam as friends
        When we query for friends of friends of Pam
        Then we get Pam as friends of friends

    Scenario: Querying FoF of non-existent person results in an error message
        Given a network
        And with Jan as a person
        And with Joe as a person
        And with Jan and Joe as friends
        When we query for friends of friends of Tom
        Then we get an error message saying "There is no person named Tom"
