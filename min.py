def min_n_variables(elements):
    second = elements[0]
    for x in elements:
      if x < second:
       second = x
    return second

elements = [3,5,8,4,9,6]
print('second of elements=', min_n_variables(elements))
 