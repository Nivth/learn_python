try:
    print('try...')
    r = 10 / int('a')  # it will throw an exception, change a to 5
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
