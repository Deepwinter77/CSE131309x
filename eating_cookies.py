# Eating all the Cookies
number_of_cookies=int(input("How Many Cookies are in the Jar? "))
cookies_eaten=0
while number_of_cookies > 0 :
    number_of_cookies = number_of_cookies -1
    cookies_eaten=cookies_eaten+1
    print("Eating cookie number ", cookies_eaten)
print ("I ate all the cookies. ")    


