nums=[str(17560),str(44358),str(41092),str(25731),str(78697),str(22171),str(90389),str(53970),str(96275)]
answers=[]
for i in range(10000,100000):
    str_i=str(i)
    total_same_count=0
    for nums_rep in range(9):
        same_count=0
        for num_rep in range(5):
            if str_i[num_rep]==nums[nums_rep][num_rep]:
                same_count+=1
            if same_count>1:
                break
        if same_count==1:
            total_same_count+=1
    if total_same_count==9:
        print(str_i)
        answers+=[str_i]

print(answers,'\n',
      len(answers))