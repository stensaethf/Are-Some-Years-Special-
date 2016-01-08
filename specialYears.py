'''
specialYears.py
Frederik Roenn Stensaeth
01.03.16

An investigation into whether some years/ numbers are more special than others.

To Do:
- Divisors. DONE.
- Is it fast? Time. DONE. Could be faster...
- Primes. DONE.
- Relationship between divisors and number of primes? DONE.
	--> dont have this graph connected. DONE.
	--> interesting to see that 7 primes seem to be the max. Wonder why... DONE.
		--> max is 8 primes up to 100,000. DONE.
			--> first occurance is in 30030. DONE.
	--> does the relationship look similar for evens and odds? DONE.
	--> what about different types of numbers?
		---> squares.
		---> cubes.
		---> triangular (sum from k=1 to n of k).
			--> T(1) = 1
			--> T(2) = 3
			--> T(3) = 6
			--> T(4) = 10
			--> T(5) = 15
			--> T(6) = 21
			--> T(n) = n + T(n - 1)
'''

import sys
import matplotlib.pyplot as mplot
from matplotlib import style
import time

def printUsage():
	"""
	printUsage() prints out the usage message for the program.

	@params: n/a.
	@return: n/a.
	"""
	print 'Usage: $ python specialYears.py normal <start number> <end number>'
	print 'Usage: $ python specialYears.py primes <start number> <end number>'
	print 'Usage: $ python specialYears.py compare <start number> <end number>'

def isPrime(div):
	"""
	isPrime() tells whether a given number is a prime or not.

	@params: number (int).
	@return: boolean.
	"""
	for i in range(2, (div / 2) + 1):
		if div % i == 0:
			return False
	return True

def getDivisors(y_s, y_e, res, mode_num):
	"""
	getDivisors() finds the number of divisors for each number within a range
	of numbers. Can restrict to only primes is needed.

	@params: start number,
			 end number,
			 res (list to store results in),
			 prime boolean (whether to restrict to primes or not).
	@return: list with divisor counts.
	"""
	if mode_num >= 4:
		# squares, cubes, triangular.
		if (mode_num == 4) or (mode_num == 5):
			# squares, cubes.
		else:
			# triangular.
			t_n = 1
			for i in range(2, y_s):
				t_n = t_n + i
			for year in range(y_s, y_e + 1):
				t_n = t_n + year
				# code.
	else:
		# loop over each desired number and check for divisors.
		for year in range(y_s, y_e + 1):
			print year
			total = 1 # start at 1 because of division by itself.
			for num in range(1, (year / 2) + 1):
				if (0 == year % num):
					if mode_num == 1:
						if isPrime(num):
							total += 1
					elif mode_num == 2:
						if year % 2:
							total += 1
					elif mode_num == 3:
						total += 1
					elif mode_num == 4:
						# squares.
					elif mode_num == 5:
						# cubes.
					elif mode_num == 6:
						# triangular.
					else: # 0
						total += 1
			res.append(total)
	return res

def main():
	# usage: $ python specialYears.py normal <start number> <end number>
	# usage: $ python specialYears.py primes <start number> <end number>
	# usage: $ python specialYears.py compare <start number> <end number>
	if len(sys.argv) != 4:
		print 'Error. Invalid number of arguments given.'
		printUsage()
		sys.exit()

	# Changing the style gives us a nicer looking backframe for the graph.
	style.use('ggplot')

	figure = mplot.figure()
	actual_plot = figure.add_subplot(1, 1, 1)

	# get the command line arguments and do necessary error checks.
	try:
		mode = sys.argv[1]
		y_s = int(sys.argv[2])
		y_e = int(sys.argv[3])
	except:
		print 'Error. Problem with arguments given.'
		printUsage()
		sys.exit()

	if y_e < y_s:
		print 'Error: end < start.'
		printUsage()
		sys.exit()
	elif y_s < 1:
		print 'Error: start number < 0.'
		printUsage()
		sys.exit()

	t_s = time.time()
	if mode == 'normal':
		# normal mode.
		res = getDivisors(y_s, y_e, [], 0)
		mplot.ylabel('Divisors')
	elif mode == 'primes':
		# primes mode.
		res = getDivisors(y_s, y_e, [], 1)
		mplot.ylabel('Primes')
	elif mode == 'compare':
		# compare mode.
		# x-axis: all divisors.
		# y-axis: primes.
		x_values = getDivisors(y_s, y_e, [], 0) # all divisors
		res = getDivisors(y_s, y_e, [], 1) # primes

		actual_plot.scatter(x_values, res) # scatter
		mplot.xlabel('Divisors')
		mplot.ylabel('Primes')
		mplot.show()
		return
	elif mode == 'odd':
		# odd mode.
		res = getDivisors(y_s, y_e, [], 2)
		mplot.ylabel('Odds')
	elif mode == 'even':
		# even mode.
		res = getDivisors(y_s, y_e, [], 3)
		mplot.ylabel('Evens')
	elif mode == 'square':
		# square mode.
		res = getDivisors(y_s, y_e, [], 4)
		mplot.ylabel('Squares')
	elif mode == 'cube':
		# cube mode.
		res = getDivisors(y_s, y_e, [], 5)
		mplot.ylabel('Cubes')
	elif mode == 'triangular':
		# triangular mode.
		res = getDivisors(y_s, y_e, [], 6)
		mplot.ylabel('triangulars')
	else:
		print 'Error: mode.'
		printUsage()
		sys.exit()
	t_f = time.time()

	# testing
	print('Time to run: ' + str(t_f - t_s) + 'sec.')
	print('Number with highest number of divisors: ' + str(res.index(max(res)) + y_s) + '.')
	print('Number of divisors for that number: ' + str(max(res)) + '.')

	x_values = [yr for yr in range(y_s, y_e + 1)]

	# plot the results
	actual_plot.plot(x_values, res, 'k')
	mplot.xlabel('Number')
	mplot.show()


if __name__ == '__main__':
	main()