# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
 if len(lst) >= 1:
        lst.remove(lst[0])  
    if len(lst) >= 5:
        lst.remove(lst[4]) 
    if len(lst) >= 5:
        lst.remove(lst[4])



def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True 
    elif len(list_to_check) > 0: 
        return False 


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)<3 or len(list_to_compare2)<3:
        return False
    elif list_to_compare1[1] == list_to_compare2[1]:
        return True
    else:
        return False 
        
def list_of_lists(lists):
    if len(lists[0]) > 2:
        lists[0] = lists[0][:2]
    if len(lists[1]) > 1:
        lists[1] = lists[1][1:4]
        
    if len(lists[2]) > 2:
        lists[2] = lists[2][-2:]
    return lists
