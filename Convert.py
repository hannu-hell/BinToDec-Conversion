class Convert(object):
	def __init__(self, num):
		self.num = num 

	def to_decimal(self):
		highestIndex = len(self.num)-1
		decimalValue = 0
		for n in self.num:
			digit = int(n) * (pow(2, highestIndex))
			highestIndex -= 1
			decimalValue += digit
			if highestIndex < 0:
				return str(decimalValue)

	def to_binary(self):
		binaryList = []
		val = int(self.num)
		while val // 2 != 1:
			mod_val = val % 2
			binaryList.append(mod_val)
			val = val // 2
		if val // 2 == 1:
			mod = val % 2 
			binaryList.append(mod)
			binaryList.append(1)
			binaryList.reverse()
		for i in range(len(binaryList)):
			binaryList[i] = str(binaryList[i])
		return ''.join(binaryList)




print(Convert("100100").to_decimal())
print(Convert("36").to_binary())