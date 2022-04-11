def set_work_data(function, window_offset, left_border, right_border, step):
    current_arg = left_border
    # contains <window_offset> elements always
    current_args_list = []
    predicted_values_list = []
    # contains all possible <current_args_list> states
    all_args_list = []
    # first widow_offset values in list
    for i in range(window_offset):
        func_value = function(current_arg)
        current_args_list.append(func_value)
        current_arg += step
    # create train data and deal with rest of values
    while current_arg < right_border:
        func_value = function(current_arg)

        all_args_list.append(current_args_list.copy())
        predicted_values_list.append(func_value)

        current_args_list.pop(0)
        current_args_list.append(func_value)

        current_arg += step
    return list(zip(all_args_list, predicted_values_list))


def set_dots(function, left_border, right_border, step):
    arg = left_border
    arg_list = []
    value_list = []
    while arg < right_border:
        arg_list.append(arg)
        value_list.append(function(arg))
        arg += step
    return [arg_list, value_list]
