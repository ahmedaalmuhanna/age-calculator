from datetime import date, timedelta

import datetime
def get_dob():
    
    # write code here
	bdy = input("Enter year of birth: ")
	bdm = input("Enter month of birth: ")
	bdd = input("Enter day of birth: ")
	print(type(int(bdy)))
	if bdy.isdigit() and bdm.isdigit() and bdd.isdigit() :
			print(type(date.today()))
			
			print(datetime.date(int(bdy),int(bdm),int(bdd)))
   
			return datetime.date(int(bdy),int(bdm),int(bdd))
	else:
			print("your input is invalid")
			return 0

def get_age(date):
	print(date)


	return date.today()- date

def main():

	print(get_age(get_dob()))


if __name__ == '__main__':
    main()
