*** Settings ***
Library     ../../modules/Outlook_API/steps/RequestStepDef.py
Library     ../../modules/Outlook_API/steps/ResponseStepDef.py
Variables  variables.py
*** Variables ***
#${ACCOUNT}   andy.bazualdo@jalasoftdevelopment.onmicrosoft.com
${ACCOUNT}   ${email}
${PARAMS}   ${filterSubject}
${JSON}   ${emailToSent}
${SUBJECT}   ${subj}
${SUBJECT2}   ${subj2}

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
    send_get_request_with_wait_time  /users/{value}/mailFolders/sentitems/messages   ${account}
    the email subject is  ${subject2}

Open mail
    [Arguments]  ${account}  ${params}  ${subject}

    user authentication
    send get request to  /users/{value}/messages   ${account}  ${PARAMS}
    i should see the status code as  200
    the email subject is  ${subject}