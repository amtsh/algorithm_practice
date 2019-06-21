def int_to_roman(input):
  """ Convert an integer to a Roman numeral. """

  ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10, 9, 5, 4, 1)
  romans = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
  result = []
  for i in range(len(ints)):
      count = int(input / ints[i])
      result.append(romans[i] * count)

      input -= ints[i] * count

  return ''.join(result)

def roman_to_int(input):
  """ Convert an integer to a Roman numeral. """

  roman = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
  sum = 0

  for idx in range(len(input)):
    current_value = roman[input[idx]]

    if idx < len(input) - 1 and current_value < roman[input[idx + 1]]:
      sum -= current_value
    else:
      sum += current_value

  return sum

print(int_to_roman(9) == 'IX')
print(roman_to_int('IX') == 9)
