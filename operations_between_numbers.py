number=int(input())
number2=int(input())
opeator=input()
end_sum=number+number2
end=number-number2
end_thing=number*number2
end_divide=number/number
end_percent=number%number2
if opeator=="+":
    if end_sum%2==0:
        print(f"{number}{opeator}{number2}={end_sum} - even")
    else:
         print(f"{number}{opeator}{number2}={end_sum} - odd")
elif opeator=="-":
    if end_sum%2==0:
        print(f"{number}{opeator}{number2}={end} - even")
    else:
         print(f"{number}{opeator}{number2}={end} - odd")
elif opeator=="*":
    if end_sum%2==0:
        print(f"{number}{opeator}{number2}={end_thing} - even")
    else:
         print(f"{number}{opeator}{number2}={end_thing} - odd")
elif opeator=="/":
    if number2==0:
        print(f"Cannot divide {number} by zero")
    else:
        print(f"{number}{opeator}{number2}={end_divide:.2f}")
elif opeator=="%":
    if number2==0:
        print(f"Cannot divide {number} by zero")
    else:
        print(f"{number}{opeator}{number2}={end_percent}")
