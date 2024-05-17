# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    lista= []
    
    # Agregar el primer elemento si existe
    if len(list_to_remove_elements) > 0:
        lista.append(lst[0])
    if len(list_to_remove_elements) > 4:
        lista.append(lst[4])
    if len(list_to_remove_elements) > 5:
        lista.append(lst[5])
    result = list_to_remove_elements[:]
    for element in elements_to_remove:
        result.remove(element)



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
    elif list_to_compare1[2] == list_to_compare2[2]:
        return True
    else:
        return Flase 

def list_of_lists(list_of_lists_to_modify):
   list1= list_of_lists_to_modify[0][0:2]
   list2= list_of_lists_to_modify[1][1:4]
   list3= list_of_lists_to_modify[2][-2::]
   final_list= [list1, list2, list3]
    return final_test
