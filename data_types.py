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