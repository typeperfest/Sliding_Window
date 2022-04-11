from train_data import set_work_data
from train_data import set_dots

from plt_graphs import make_plot
from plt_graphs import make_frequency
from plt_graphs import make_graph
from plt_graphs import show_figures

from neuro_base import PlaneNeuralNetwork


def main_function(arg):
    return arg ** 4 - 2 * arg ** 3 + arg


if __name__ == "__main__":
    error = 0.001  # 0.1, 0.04, 0.01, 0,001, 0,0001
    window_offset = 6
    a = -0.5
    b = 0.5
    step = (b - a) / 20
    training_normal = 0.4
    train_data = set_work_data(main_function, window_offset, a, b, step)
    neural_network = PlaneNeuralNetwork([0] * window_offset, 0, training_normal)
    train_eras = neural_network.train(train_data, error)
    # Show results of train
    make_graph(a, 2 * b - a, main_function)
    args, values = set_dots(main_function, a, b, step)
    make_frequency(args, values, 'r')
    # Now check network's prediction abilities
    check_data = set_work_data(main_function, window_offset, b - step * window_offset, 2 * b - a, step)
    predicted_arg = b - step
    predicted_values_list = []
    predicted_args_list = []
    for test in check_data:
        predicted_arg += step
        predicted_args_list.append(predicted_arg)
        predicted_value = neural_network.get_result(test[0])
        predicted_values_list.append(predicted_value)
    make_frequency(predicted_args_list, predicted_values_list, 'g')
    # Show all graphs
    show_figures()
