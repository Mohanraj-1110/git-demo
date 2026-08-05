#!/usr/bin/env python3
"""Simple swap value program.

Usage examples:
  - Run and enter two values when prompted.
  - Or call swap_values(a, b) from other code.
"""

def swap_temp(a, b):
	"""Swap using a temporary variable."""
	temp = a
	a = b
	b = temp
	return a, b


def swap_tuple(a, b):
	"""Swap using tuple unpacking (Pythonic)."""
	return b, a


def swap_arithmetic(a, b):
	"""Swap numbers using arithmetic (works for ints/floats).
	Note: may overflow for extremely large ints in some languages, but OK in Python.
	"""
	a = a + b
	b = a - b
	a = a - b
	return a, b


def main():
	try:
		x = input('Enter first value: ')
		y = input('Enter second value: ')
	except (EOFError, KeyboardInterrupt):
		print()
		return

	print('\nOriginal:', x, y)
	a, b = swap_tuple(x, y)
	print('Swapped (tuple):', a, b)

	# Try numeric arithmetic swap if inputs are numbers
	try:
		nx, ny = float(x), float(y)
	except ValueError:
		return

	a2, b2 = swap_temp(nx, ny)
	print('Swapped (temp):', a2, b2)
	a3, b3 = swap_arithmetic(nx, ny)
	print('Swapped (arithmetic):', a3, b3)


if __name__ == '__main__':
	main()

