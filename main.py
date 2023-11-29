Cuisine = {}

for x in range(3):
  country = input('What country do you want food from? ')
  dish = input('What food do you want? ')
  Cuisine[ country ]  = dish

print('Here is your dish. ')
print(Cuisine)

if 'spaghetti' in Cuisine.keys():
    print('This is the best food ever')
else: 
    print( 'I think you forgot something, I\'ll add it: ')
    Cuisine['spahgetti'] = 'dish'
    print(Cuisine)

print('Bye! please come again. ')
