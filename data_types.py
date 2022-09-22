string_a = ['this is ', 'the first', 'string of strings', 'the test']
string_b = ['not a ', ' long string', "but it's", 'close enough' ]

def find_test(the_thing):
    for string_1 in the_thing:
        if(string_1.endswith('test')):
            print(string_1, 'found test')
        else:
            print(string_1, 'no test')

find_test(string_b)

find_test(string_a)

# # if ((string_a.endswith('test')) or (string_b.endswith('test'))):
# #     print( 'found test')
# # else:
#     print('no test')


list_numbers = [1, 3, 5, 7, 11, 13, 17, 19, 21, 25, 27]

for num in list_numbers:
    if(num > 10):
        print('large:', num)
    elif(num <= 10):
        print('not large:', num)

