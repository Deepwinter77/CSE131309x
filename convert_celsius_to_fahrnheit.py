# This program converts Celsius to Fahrenheit
user_response=input("Please input a temperature in celsius :")
celsius=float(user_response)
fahrenheit=((celsius*9) / 5) + 32
print("The temperature is ",fahrenheit," degrees Fahrenheit.")
if fahrenheit<32 :
    print("It is freezing")
elif fahrenheit<50 :
    print("It is chilly")
elif fahrenheit<90 :
    print("It is ok")
else :
    print("It is hot")
