import random
import string

def main():
	password(7)

def password(length):
	for x in range (0, length):
		print (random.choice(string.ascii_letters), end = '')

if __name__ == '__main__':
	main()
