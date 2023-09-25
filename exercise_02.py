our_numbers = [9, 1, 2, 3, 8, 1, 15]
sum_of_three = []
end_step = 2
                                             
for i in range(len(our_numbers) - end_step): #[9, 1, 2, 3, 8, 1]
    summary = 0
    for j in range(i,i+3):
            summary += our_numbers[j]

    sum_of_three.append(summary)

circle_list = our_numbers[end_step + 1:] + our_numbers[:end_step]

for t in range(len(circle_list) - end_step):
    summary = 0
    for n in range(t,t+3):
        summary += circle_list[n]
    sum_of_three.append(summary)

find_max = sum_of_three[0]

for el in range(len(sum_of_three)):
     if sum_of_three[el] > find_max:
          find_max = sum_of_three[el]

print(find_max)
