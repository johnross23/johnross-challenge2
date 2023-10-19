#Johnross Francis Bomboka
#This program prompts the user to enter two integer  values
#And greater number will be returned


def main():
    title='GREATER NUMBERS'
    print(title)
    number_1 = int(input( ' Enter the first number'))
    number_2 = int(input(' Enter the second number'))

    #returning numbers
    
    return number_1,number_2


def max(number_1,number_2):
    if number_1 >= number_2:
        print('The greater number is:',number_1)
    else:
        print('The greater number is:',number_2)

number_1,number_2 = main()
max(number_1,number_2)
