def explore_list_changes(some_list): 
    print(f"  Inside function (start): some_list id={id(some_list)}, some_list={some_list}")
    some_list.append(4)
    print(f"  Inside function (after append): some_list id={id(some_list)}, some_list={some_list}")


    some_list = [5, 6, 7]
    print(f"  Inside function (after reassignment): some_list id={id(some_list)}, some_list={some_list}")
    some_list.append(8)
    print(f"  Inside function (after second append): some_list id={id(some_list)}, some_list={some_list}")
    return some_list

my_numbers = [1, 2, 3] 
print(f"Before function call: my_numbers id={id(my_numbers)}, my_numbers={my_numbers}")
returned_list_result = explore_list_changes(my_numbers) 
print(f"After function call: my_numbers id={id(my_numbers)}, my_numbers={my_numbers}")
print(f"Returned list result: returned_list_result id={id(returned_list_result)}, returned_list_result={returned_list_result}")
print("-" * 30)


current_value = 8
shifted_value = current_value >> 1 
print(f"Original current_value: {current_value}")
print(f"current_value >> 1 (right shift by 1): {shifted_value}")
print("-" * 30)

my_list_example = [1, 2, 3] 
print(f"Initial my_list_example: {my_list_example}")
removed_element = my_list_example.pop() 
print(f"Removed element: {removed_element}")
print(f"my_list_example after pop: {my_list_example}")
print("-" * 30)

def grow_list_in_place(the_list_to_grow): 
    """
    This function adds new elements right into the list you give it.
    """
    print(f"  Inside function (start): the_list_to_grow id={id(the_list_to_grow)}, the_list_to_grow={the_list_to_grow}")
    the_list_to_grow += [4, 5, 6]
    print(f"  Inside function (end): the_list_to_grow id={id(the_list_to_grow)}, the_list_to_grow={the_list_to_grow}")

my_data_collection = [1, 2, 3]
print(f"Before function call: my_data_collection id={id(my_data_collection)}, my_data_collection={my_data_collection}")
grow_list_in_place(my_data_collection) 
print(f"After function call: my_data_collection id={id(my_data_collection)}, my_data_collection={my_data_collection}")
print("-" * 30)

print("Looping with range(1, 6, 2):")
for number in range(1, 6, 2): 
    print(number)
print("-" * 30)

some_raw_text = "hello\n  world\n  this\n is\n  python " 
print(f"Original some_raw_text:\n'''{some_raw_text}'''")
text_lines = some_raw_text.split('\n') 
print(f"List of text_lines after split: {text_lines}")
cleaned_up_line = text_lines[4].strip() 
print(f"Cleaned 5th line (index 4): '{cleaned_up_line}'")
print("-" * 30)

my_settings = {'a': 1, 'b': 2, 'c': 3, 'a': 9} 
print(f"My settings dictionary: {my_settings}")
print(f"Value for key 'a': {my_settings['a']}")
print("-" * 30)

my_number_list = [10, 20, 30, 40, 50] 
print(f"Original my_number_list: {my_number_list}")
the_last_three = my_number_list[-3:] 
print(f"Last three elements (my_number_list[-3:]): {the_last_three}")
print("-" * 30)

my_tuple_of_values = (10, 20, 30, 40, 50) 
print(f"Original my_tuple_of_values: {my_tuple_of_values}")
print("Attempting to modify a tuple element directly will result in a TypeError.")
a_new_tuple_with_change = my_tuple_of_values[:-1] + (100,) 
print(f"New tuple created with last element modified: {a_new_tuple_with_change}")
print("-" * 30)


def generate_numbers_one_by_one(): 
    for i in range(5):
        yield i

my_number_generator = generate_numbers_one_by_one() 
print("Iterating through the generator:")
for generated_value in my_number_generator: 
    print(generated_value)
print("-" * 30)