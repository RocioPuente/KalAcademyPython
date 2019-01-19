minutes= eval(input("Enter the number of minutes:"))
day= minutes / 1440
year= (day // 365)
days= day % 365

print (minutes, "minutes is approximetely ", int(year), "years and", int(days), "days")
