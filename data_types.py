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


group_clients = {
    'username': 'userOne',
    'age': 22,
    'friends': ['bob', 'peter', 'jane', 'bruce']
}

print(group_clients['username'], group_clients['age'])

for friend in group_clients['friends']:
    print(friend)

client = [
    {
    'username': 'userOne',
    'age': 22,
    'friends': ['bob', 'peter', 'jane', 'bruce']
},
{
    'username': 'userTwo',
    'age': 23,
    'friends': ['bob2', 'peter2', 'jane2', 'bruce2']
},
{
    'username': 'userThree',
    'age': 24,
    'friends': ['bob3', 'peter3', 'jane3', 'bruce3']
},
{
    'username': 'userFour',
    'age': 25,
    'friends': ['bob4', 'peter4', 'jane4', 'bruce4']
}
]

for one_client in client:
    print(one_client['username'], one_client['age'], one_client['friends'])