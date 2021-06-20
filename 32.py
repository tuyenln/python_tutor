def calc_total_price(apple_weight, PRICE):
	return apple_weight * PRICE

def calcBack(total_price ,moneyIn):
	if moneyIn < total_price:
		return -1

	return moneyIn - total_price

def show_return_info(total):
	count_500 = int(total/500)
	total = total - 500 * count_500
	if count_500 != 0:
		print("500K : " + str(count_500))

	count_200 = int(total/200)
	total = total - 200 * count_200
	if count_200 != 0:
		print("200K : " + str(count_200))

	count_100 = int(total/100)
	total = total - 100 * count_100
	if count_100 != 0:
		print("100K : " + str(count_100))

	count_50 = int(total/50)
	total = total - 50 * count_50
	if count_50 != 0:
		print("50K : " + str(count_50))

	count_20 = int(total/20)
	total = total - 20 * count_20
	if count_20 != 0:
		print("20K : " + str(count_20))

	count_10 = int(total/10)
	total = total - 10 * count_10
	if count_10 != 0:
		print("10K : " + str(count_10))

	count_1 = int(total)
	print("1K : " + str(count_1))



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
		show_return_info(backmoney)


main()

