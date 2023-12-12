*** Settings ***
Library  SeleniumLibrary
Resource  ../Variables/Variable.robot
Resource  ../Helpers/Helpers.robot

*** Keywords ***
opening browser
    Open Browser    ${URL}  ${browser}
    maximize browser window
    wait for and click on element    ${Cancel_button}   5
# use scrollinto view later
    Mouse Over   ${produc_category}
    wait for and click on element    ${products}    3
    wait for and click on element    ${item}    2
    ${windows}=     Get Window Handles
    Switch Window   ${windows}[1]
    ${title}=     Get Title
    ${message}=     Get Text    ${text}
    log to console    ${message}
    Page Should Contain     ${message}
    wait for and click on element   ${size}     6
    sleep   5
    wait for and click on element   ${cart}     2

#    wait for and click on element    ${size_chart}    2
#    ${chest}=   Get Text    ${size}
#    log to console  ${chest} SIZE VALUE
#    ${elements}=    Get Webelements  ${sizes_available}
#    log to console      ${elements}
#    FOR  ${i}  IN   ${elements}
#        ${texts}=    Get Text   //a[@class='_1fGeJ5 _2UVyXR _31hAvz']
#        EXIT FOR LOOP IF    ${texts} == ${chest}
#    END
#    Click Element       ${i}
#    log     ${title}
#    log to console  ${title}


