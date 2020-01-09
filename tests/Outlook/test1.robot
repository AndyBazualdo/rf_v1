*** Settings ***
Resource  ../Outlook/keywords.robot
Suite Setup     Open Home Page
Suite Teardown  Close Browsers


*** Test Cases ***
User login
   [Tags]	   Login Test
    Given access to sign in button
    When set user email account  ${USER_MAIL_G}
    And set user password account  ${USER_PASS_G}
    Then user loged is  ${USER_MAIL_G}

Open Outlook
    [Tags]	   Open Outlook
    Given app menu is visible
    When outlook app is opened
#    and get app title
    Then app title is  Outlook

Send Mail
    [Tags]	   Send Mail
    Given window new message is open
    When set destination mail   andy1@mailinator.com
    And set mail subject  testAUT
    And set boby content  text
    And send test email
    Then verify email was sent  andy1@mailinator.com  testAUT

#    Send message  andy1@mailinator.com   testAUT   text
#
Open Mail
    [Tags]	   Open Mail
    Given open inbox section
    When open received email with subject  testing new account
    Then validate received email can be opened  testing new account

#    Open message  testing new account