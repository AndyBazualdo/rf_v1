*** Settings ***
#Library     SeleniumLibrary
Library     ../../modules/Outlook/steps/CommonSteps.py
Library     ../../modules/Outlook/steps/LoginSteps.py
Library     ../../modules/Outlook/steps/OutlookMailSteps.py
Variables  variables.py
*** Variables ***
${URL}        ${urlFile}
${BROWSER}    ${browserFile}
${USER_MAIL_G}  ${userMailFile}
${USER_PASS_G}   ${userPassFile}
${title}
*** Keywords ***
Open Home Page
#    Set Selenium Speed  1.5 seconds
    Open

Close Browsers
    Close All

Set user email
    [Arguments]      ${user_mail}  ${user_pass}
     access to sign in button
     set user email account  ${user_mail}
     set user password account  ${user_pass}
     user loged is  ${user_mail}

#Validate login
#    [Arguments]      ${user_mail}
#    Click Element  css:[id='O365_MainLink_MePhoto']
#    ${account}  Get Text  css:[title='${user_mail}']
#    Should Be Equal As Strings  ${account}   ${user_mail}
#
Open Outlook
     app menu is visible
     outlook app is opened
#     ${res} =  get app title
     app title is  "${title}"
#    ${appname}  Get Text  css:a[id='O365_AppName'] span
#    Should Be Equal As Strings  Outlook   ${appname}
#
Send message
    [Arguments]  ${mail}  ${subject}  ${body}
    window new message is open
    set destination mail   ${mail}
    set mail subject  ${subject}
    set boby content  ${body}
    send test email
    verify email was sent  ${mail}  ${subject}


#    Click Element  css:span[id='id__3']
#    Input Text  xpath://div[contains(text(), 'To')]//following::input[1]  ${mail}
#    Input Text  css:#subjectLine0  ${subject}
#    Input Text  css:div[aria-label='Message body'] div  ${body}
#    Click Element  css:button[aria-label='Send']
#    Click Element  xpath://i[@data-icon-name='Send'][1]
#    ${text} =  Get Element Attribute  xpath://div[contains(text(), 'To')]//following::div[1]  aria-label
#    Should Contain  ${text}  ${mail}
#    Should Contain  ${text}  ${subject}
#
Open message
    [Arguments]  ${subject}
    open inbox section
    open received email with subject  "${subject}"
    validate received email can be opened  "${subject}"

#    Click Element  xpath://i[@data-icon-name='Inbox'][1]
#    Click Element  xpath://div[@role='option' and contains(@aria-label, '${subject}')]
#    ${title} =  Get Element Attribute  xpath://div[@role='heading' and contains(@title,'testing new account')]  title
#    Should Be Equal As Strings  ${title}   ${subject}