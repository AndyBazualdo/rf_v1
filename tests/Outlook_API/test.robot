*** Settings ***
Resource  keywords.robot
#Suite Setup     user authentication
#Suite Teardown  Close Browsers


*** Test Cases ***
user authentication and logged
    [Tags]	Login Test

    Given user authentication
    When send get request to  /users/{value}   ${account}
    And i should see the status code as  200
    Then the value is equal to   userPrincipalName  ${account}

Outlook access
    [Tags]  Outlook access

    Given user authentication
    When send get request to  /users/{value}/mailFolders   ${account}
    And i should see the status code as  200
    Then the value is not null  value

Outlook Send mail
    [Tags]  Send mail

    Given user authentication
    When send post request to  /users/{value}/sendMail   ${account}  ${JSON}
    And i should see the status code as  202


Outlook Open mail
    [Tags]  Open mail

    Given user authentication
    When send get request to  /users/{value}/messages   ${account}  ${params}
    And i should see the status code as  200
