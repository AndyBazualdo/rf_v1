*** Settings ***
Library  ../modules/project/pages/SearchFlightPage.py

*** Keywords ***
Open search page
    open

Close pages
    close

Select departure
    [Arguments]  ${city}

    select departure city  ${city}

select destination
    [Arguments]  ${city}
    select destination city  ${city}

Search Flights
    search for flights
    @{flights}=     Get Found Flights
    set test variable  ${flights}

Flights are found
    Should Not Be Empty     ${flights}