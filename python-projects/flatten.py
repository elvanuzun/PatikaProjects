flat_list = []

def flatten_func(given_list):
  for item in given_list:
        if isinstance(item, list):
            flatten_func(item)
        else:  
            flat_list.append(item)
    
    
my_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
(flatten_func(my_list))
print(flat_list)
