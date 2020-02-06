*** Settings ***
Library     ../../modules/Outlook_API/steps/RequestStepDef.py
Library     ../../modules/Outlook_API/steps/ResponseStepDef.py
Variables  variables.py
*** Variables ***
#${ACCOUNT}   andy.bazualdo@jalasoftdevelopment.onmicrosoft.com
${ACCOUNT}   ${email}
${PARAMS}   ${filterSubject}
${JSON}   ${emailToSent}

*** Keywords ***
Login Test
   [Arguments]  ${account}
    user authentication
    send get request to  /users/{value}   ${account}
    i should see the status code as  200
    the value is equal to   userPrincipalName  ${account}

Outlook access
   [Arguments]  ${account}
   user authentication
   send get request to  /users/{value}/mailFolders   ${account}
   i should see the status code as  200
   the value is not null  value

Outlook Send mail
    [Arguments]  ${account}
    user authentication
    send post request to  /users/{value}/sendMail   ${account}  ${JSON}
    i should see the status code as  202

Open mail
    [Arguments]  ${account}  ${params}

    Given user authentication
    When send get request to  /users/{value}/messages   ${account}  ${PARAMS}
    And i should see the status code as  200