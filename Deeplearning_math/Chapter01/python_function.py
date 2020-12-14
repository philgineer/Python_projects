def extractor(input_list, cutoff_min, cutoff_max):
    return_list = []
    for val in input_list:
        if val >= cutoff_min and val < cutoff_max:
            return_list.append(val)
            
    return return_list
    
tmp_list = [i for i in range(100)]
for cutoff_min in range(0, 70, 10):
    e_list = extractor(tmp_list, cutoff_min, cutoff_min + 10)
    print(e_list)