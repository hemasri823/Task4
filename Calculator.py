print("""Select Arithmetic operation:
              1.Addition
              2.Subtraction
              3.Multiplication
              4.Division
              5.Modulus""")
def print_answer(one,two,operation,answer):
    print(one,operation,two,"=",answer)



while True:
        selection = int(input("select arithmetic operation: "))
        if selection in (1,2,3,4,5):
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            if selection==1:
                answer = first_number+second_number
                print_answer(first_number,second_number,"+",answer)
            elif selection==2:
                answer = first_number - second_number
                print_answer(first_number, second_number, "-", answer)
            elif selection == 3:
                answer = first_number * second_number
                print_answer(first_number,second_number,"*",answer)
            elif selection==4:
                answer = first_number / second_number
                print_answer(first_number,second_number,"/",answer)
            elif selection==5:
                answer = first_number % second_number
                print_answer(first_number,second_number,"%",answer)
            another_calculation = input("Would u like to make another calculation? (1.Yes/2.No): ")
            if another_calculation == "2":
                break
        else:
            print("Make selection from list provider")