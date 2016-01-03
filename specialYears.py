'''
specialYears.py
Frederik Roenn Stensaeth
01.03.15

An investigation into whether some years are more special than others.

To Do:
- Divisors.
- Dynamic programming solution.
- Which is faster?
'''

import sys

def main():
	# usage: $ python specialYears.py normal <start year> <end year> ...
	# usage: $ python specialYears.py dynamic <start year> <end year> ...

	mode = sys.argv[1]
	y_s = int(sys.argv[2])
	y_e = int(sys.argv[3])

	if y_e < y_s:
		print 'Error: end < start'
		sys.exit()

	res = []
	if mode == 'normal':
		for year in range(y_s, y_e):
			total = 0
			for num in range(1, (year / 2) + 1):
				if 0 == year % num:
					total += 1
			res.append(total)
	else:
		print 'Error: mode'
		sys.exit()
	print(res)

if __name__ == '__main__':
	main()