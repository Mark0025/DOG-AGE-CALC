#1. we want to get the dogs age
#2. we need to create function to calculate the age in dog years
#3. we need to print the age in dog years


def main():
    def calculate_dog_age(age_of_dog):
        #1 1st human year = 15 dog years
        #2. 2nd human year = 9 dog years
        #3. every year after that is 5 dog years

        # if dog is less than or equal to 2
        if age_of_dog <= 1:
            dog_age = age_of_dog * 15
        elif age_of_dog <= 2:
            dog_age = 15 + 9
        else:
            dog_age = 15 + 9 + (age_of_dog - 2) * 5
        return dog_age

    while True:
        dog_name = input("What is your dog's name? ")
        age_of_dog = int(input(f"How old is {dog_name} in human years? "))
        
        dog_age = calculate_dog_age(age_of_dog)
        print(f"{dog_name} is {dog_age} years old in dog years!")
        
        calculate_another = input("Would you like to calculate another dog's age? (yes/no) ").lower()
        if calculate_another != 'yes':
            print("Thank you for using the dog age calculator!")
            break

if __name__ == "__main__":
    main()