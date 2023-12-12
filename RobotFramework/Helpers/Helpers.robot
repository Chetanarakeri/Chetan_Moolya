*** Settings ***
Library     SeleniumLibrary
Resource  ../Variables/Variable.robot
Resource  ../Keywords/keyword.robot

*** Keywords ***
wait for and click on element
     [Arguments]    ${element1}     ${time}
     Wait Until Element Is Visible   ${element1}    ${time}
     Click Element  ${element1}
