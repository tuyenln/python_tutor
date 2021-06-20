def calc_total_price(apple_weight, PRICE):
	return apple_weight * PRICE

def calcBack(total_price ,moneyIn):
	if moneyIn < total_price:
		return -1

	return moneyIn - total_price

def show_return_info(total):



def main():
	PRICE = 21
	apple_weight =  input("Enter weight of apples: ")
	moneyGiven = input("Total money customer give you: ")
	moneyGiven = float(moneyGiven)
	apple_weight = float(apple_weight)

	total_price = calc_total_price(apple_weight, PRICE)
	backmoney = calcBack(total_price, moneyGiven)

	if backmoney == -1:
		print("Not enought moeny")
	else:
		print("You need return :" + str(backmoney))


main()