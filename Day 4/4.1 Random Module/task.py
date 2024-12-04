import random
random_integer=random.randint(1,5)
rand_float=random.random()*5
random_float_uni=random.uniform(0,5)
print(random_integer)
print(rand_float)
print(random_float_uni)

# print head or tail
head_or_tail=['head','tail']
rand_result=head_or_tail[random.randint(0,1)]
print(rand_result)
# who will pay
friends = ['alice','bob','charlie','david','emanuel']
today_bill_goes_to=friends[random.randint(0,len(friends)-1)]
print(f'Today bill goes to {today_bill_goes_to}')
list_one=[1,2,3]
list_two=[4,5,6]
list_final=list_one+list_two
print(list_final)
