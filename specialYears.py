'''
specialYears.py
Frederik Roenn Stensaeth
01.03.16

An investigation into whether some years/ numbers are more special than others.

To Do:
- Divisors. DONE.
- Is it fast? Time. DONE. Could be faster...
- Primes. DONE
- Relationship between divisors and number of primes? ALMOST DONE.
	--> dont have this graph connected.
	--> interesting to see that 7 primes seem to be the max. Wonder why...
	--> does the relationship look similar for evens and odds?
	--> what about different types of numbers?
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

def getDivisors(y_s, y_e, res, prime_bol):
	"""
	getDivisors() finds the number of divisors for each number within a range
	of numbers. Can restrict to only primes is needed.

	@params: start number,
			 end number,
			 res (list to store results in),
			 prime boolean (whether to restrict to primes or not).
	@return: list with divisor counts.
	"""
	# loop over each desired number and check for divisors.
	for year in range(y_s, y_e + 1):
		total = 1 # start at 1 because of division by itself.
		for num in range(1, (year / 2) + 1):
			if (0 == year % num):
				if prime_bol:
					if isPrime(num):
						total += 1
				else:
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

	x_values = [yr for yr in range(y_s, y_e + 1)]
	t_s = time.time()
	if mode == 'normal':
		# normal mode.
		res = getDivisors(y_s, y_e, [], False)
	elif mode == 'primes':
		# primes mode.
		res = getDivisors(y_s, y_e, [], True)
	elif mode == 'compare':
		# compare mode.
		# x-axis: all divisors.
		# y-axis: primes.
		x_values = getDivisors(y_s, y_e, [], False) # all divisors
		res = getDivisors(y_s, y_e, [], True) # primes

		actual_plot.scatter(x_values, res) # scatter
		mplot.show()
		return
	else:
		print 'Error: mode.'
		printUsage()
		sys.exit()
	t_f = time.time()

	# testing
	print('Time to run: ' + str(t_f - t_s) + 'sec.')
	print('Number with highest number of divisors: ' + str(res.index(max(res)) + y_s) + '.')
	print('Number of divisors for that number: ' + str(max(res)) + '.')

	# plot the results
	actual_plot.plot(x_values, res, 'k')
	mplot.show()


if __name__ == '__main__':
	main()