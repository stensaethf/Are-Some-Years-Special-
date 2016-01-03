'''
specialYears.py
Frederik Roenn Stensaeth
01.03.16

An investigation into whether some years are more special than others.

To Do:
- Divisors.
- Dynamic programming solution.
- Which is faster?
'''

import sys
import matplotlib.pyplot as mplot
from matplotlib import style

def main():
	# usage: $ python specialYears.py normal <start year> <end year> ...
	# usage: $ python specialYears.py dynamic <start year> <end year> ...

	# Changing the style gives us a little nicer looking backframe for the graph.
	style.use('ggplot')

	figure = mplot.figure()
	actual_plot = figure.add_subplot(1, 1, 1)

	# get the command line arguments and do necessary error checks.
	mode = sys.argv[1]
	y_s = int(sys.argv[2])
	y_e = int(sys.argv[3])

	if y_e < y_s:
		print 'Error: end < start'
		sys.exit()
	elif (y_e < 0) or (y_s < 0):
		print 'Error: year < 0'
		sys.exit()

	res = []
	x_values = []
	if mode == 'normal':
		# normal mode.
		# loop over each desired year and check for divisors.
		for year in range(y_s, y_e + 1):
			x_values.append(year)
			total = 0
			for num in range(1, (year / 2) + 1):
				if 0 == year % num:
					total += 1
			res.append(total)
	else:
		print 'Error: mode'
		sys.exit()

	# testing
	print('Maximum number of divisors: ' + str(max(res)))
	print('Year: ' + str(res.index(max(res))))

	# plot the results
	actual_plot.plot(x_values,res, 'k')
	mplot.show()


if __name__ == '__main__':
	main()