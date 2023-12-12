*** Settings ***
Resource     ../Helpers/Helpers.robot


*** Keywords ***
SimpleBookAPI

# - getting Authentication token -
    Create Session      simpleBooks   ${URL}
    ${Body}     create dictionary   clientName=chetan98769      clientEmail=chetan.kumar176591@gmail.com
    ${response}=    POST On Session     simpleBooks     ${AuthneticateEndpoint}     json=${Body}
    ${token}=    Get Value From Json    ${response.json()}     $[accessToken]
    ${AccessToken}     set variable    ${token[0]}
    set suite variable   ${AccessToken}
    log to console      ${AccessToken}

# - Getting the Books -
    Create Session      simpleBooks   ${URL}
    ${Books}    GET On Session      simpleBooks      url=${BooksEndpoint}
    log to console      ${Books.text}

# - Place the order -
    Create Session      simpleBooks   ${URL}
    ${orderbody}    create dictionary   bookId=1    customerName=chetan kumar
    ${headers}=  create dictionary      Authorization=Bearer ${AccessToken}    Content-Type=application/json
    ${OrderRes}=    POST On Session    simpleBooks    ${OrderEndpoint}  json=${orderbody}    headers=${headers}
#    log to console  ${OrderRes.text}
    ${orderid}=    Get Value From Json    ${OrderRes.json()}     $[orderId]
    ${OrderID}=     set variable    ${orderid[0]}
    set suite variable   ${OrderID}
    log to console      ${OrderID}

# - get an order -
    Create Session      simpleBooks   ${URL}
    ${headers}=  create dictionary      Authorization=Bearer ${AccessToken}    Content-Type=application/json
    ${orders}   GET On Session      simpleBooks        url=${orders123}${OrderID}   headers=${headers}
    log to console      ${orders.text}

#  - Update an order -
    Create Session      simpleBooks   ${URL}
    ${update_order_body}    create dictionary       customerName=chetan Arakeri
    ${headers}     create dictionary      Authorization=Bearer ${AccessToken}    Content-Type=application/json
    ${update_OrderRes}      PATCH On Session    simpleBooks   ${orders123}${OrderID}        json=${update_order_body}        headers=${headers}
    log to console      ${update_OrderRes}





