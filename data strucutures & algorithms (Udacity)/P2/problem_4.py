def sort_012(input_list):
    head, cur_index=0,0
    end= len(input_list)- 1
    while cur_index <= end:
        if input_list[cur_index] == 0:
            input_list[cur_index] = input_list[head]
            input_list[head] = 0
            cur_index += 1
            head += 1
        elif input_list[cur_index] == 2:           
            input_list[cur_index] = input_list[end] 
            input_list[end] = 2
            end -= 1
        else:
            cur_index += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

##test cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

sort_012([]) ## []
sort_012([None]) ## [None]