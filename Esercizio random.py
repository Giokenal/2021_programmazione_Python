import random
def random_select_nums_sample(n_list,n):
    return random.sample(n_list,n)

def random_select_nums_randint(n_list,n):
    for i in range(0,n):
        random_number= random.randint(0,len(n_list)-1)
        print(random_number)
        print(n_list[random_number])

def random_select_nums_choices(n_list,n):

        return random.choices(n_list,k=n)


n_list=['a','a','b','a','h','t','t']
selec_nums=3
new_list=[]
for element in n_list:
    if element not in new_list:
        new_list.append(element)
result_sample=random_select_nums_sample(new_list,selec_nums)


# random_select_nums_randint(n_list,selec_nums)
# print (random_select_nums_choices(n_list,selec_nums))
print (result_sample)