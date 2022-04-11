
class PlaneNeuralNetwork(object):
    """Main class of all neural_networks in this module"""
    def __init__(self, weight_seq, shift_weight, train_normal):
        self.weight_seq = weight_seq
        self.shift_weight = shift_weight
        self.train_normal = train_normal

    def train(self, train_data, target_error_value):
        era_number = 1
        while True:
            print("\t - era number:", era_number)
            combined_squared_error = self.train_era(train_data)
            era_number += 1
            if combined_squared_error < target_error_value:
                print('Target combined_squared_error is passed:', combined_squared_error)
                break
        return [era_number]

    def train_era(self, train_data):
        combined_error = 0
        for case in train_data:
            local_result = self.get_result(case[0])
            local_error = case[1] - local_result
            for i in range(len(case[0])):
                correction = local_error * case[0][i] * self.train_normal
                self.weight_seq[i] += correction
            self.shift_weight += local_error * self.train_normal
            combined_error += local_error ** 2
        return combined_error ** 0.5

    def get_result(self, arg_seq):
        assert len(arg_seq) == len(self.weight_seq)
        summary = 0
        for i in range(len(self.weight_seq)):
            summary += self.weight_seq[i] * arg_seq[i]
        return summary + self.shift_weight
