*** Variables ***
${URL}  https://www.flipkart.com/
${browser}  chrome
${Cancel_button}    xpath://span[@class='_30XB9F']
${produc_category}  xpath://*[text()='Fashion']
${products}      xpath://a[@class='_1BJVlg _11MZbx']
${item}          xpath:(//div[@class='_1xHGtK _373qXS'])[1]
${size}          xpath://a[text()='M']
${text}          xpath://span[@class='G6XhRU']
${cart}         xpath://li[@class='col col-6-12']/button
#${size_chart}   xpath://*[text()='Size Chart']
#${size}         xpath://table[@class='_2WObml']/tbody/tr[5]/td[2]/../td
#${sizes_available}      (//ul[@class='_1q8vHb'])[2]/li/a



#xpath:(//a[text()='Men Regular Fit Solid Spread Collar Casual Shirt'])[1]

#-d for storing results
#-i  to run tags