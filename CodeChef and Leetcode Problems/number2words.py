single_digits = ["zero", "one", "two", "three",
				"four", "five", "six", "seven",
				"eight", "nine"]

	
two_digits = ["", "ten", "eleven", "twelve",
			"thirteen", "fourteen", "fifteen",
			"sixteen", "seventeen", "eighteen",
			"nineteen"]

tens_multiple = ["", "", "twenty", "thirty", "forty",
				"fifty", "sixty", "seventy", "eighty",
				"ninety"]
tens_power = ["hundred", "thousand"]

num = (input())

if int(num)<10 and int(num)>0:
    print(single_digits[num])
elif int(num)>10 and int(num)<20:
    print(two_digits[(num%10)+1])
elif int(num)>20 and int(num)<100:
    print(tens_multiple[int(num[1])]+" "+single_digits[int(num[1])])
elif int(num)>100 and int(num)<1000:
    print(single_digits[int(num[0])]+" hundred "+tens_multiple[int(num[1])]+" "+single_digits[int(num[1])])
elif int(num)> 1000 and int(num)<9999:
    print(single_digits[int(num[0])]+" thousand "+ single_digits[int(num[0])+1]+" hundred "+tens_multiple[int(num[1])]+" "+single_digits[int(num[1])])
elif int(num)>9999:
    print("Out of range")
elif int(num)==0:
    print("zero")