def main():
	divisor(36)

def divisor(num):
	for x in range (1, num+1):
		if num % x == 0:
			print(x)

if __name__ == '__main__':
	main()
