#Average Number
#array - Problem
#10 ~ 20 : integer

#function (=method)
#name = cal_average
#input = array
#output return float average

def cal_average(numbers):  
  array_size = len(numbers)
  #print(array_size)
  
  sum = 0
  
  for i in range(array_size):
    sum = sum + numbers[i]
  '''
  for num in numbers:
    sum = sum + num
  '''
  #print(sum)
  average = sum / array_size
  #print(average)

  return average



#call(use) function
numbers = [10,11,12,13,14,15,16,17,18,19,20]
result = cal_average(numbers)
print(result)

#call(use) function
numbers2 = [50,11,62,13,44,119,200]
result=cal_average(numbers2)
print(result)


#call(use) function
numbers3 = [50.444,113567,62,13,44,-119,0.554]
result=cal_average(numbers3)
print(result)











numbers2 = [50,11,62,13,44,119,200]


































