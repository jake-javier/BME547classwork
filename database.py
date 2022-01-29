print("This is the database module and python calls it {}".format(__name__)) # ensures git only runs this file, not blood_calculator

## import blood_calculator as bc # imports the entire module as a name that can be called later
## import analysis # hypothetical other module with function of same name
### from blood_calculator import * # imports all the functions


from blood_calculator import check_HDL # imports only the functions specified. Can do multiple if separated by commas
HDL_value = 55 # assign a value

## classification = bc.check_HDL(HDL_value) # runs the function with the specified HDL value
## otheranswer analysis.check_HDL()

classification = check_HDL(HDL_value) # runs the function with specified HDL value
print("55 is {}".format(classification))

def function():
    print("one")

def function():
    print("two")