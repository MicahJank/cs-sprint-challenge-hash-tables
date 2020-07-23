# weights is a list of weights
# length is the length of the list
# limit is the the max value 2 weights need to equal

# i need to find two weights from the list whose sum is equal to the limit - done in linear time

# PLAN
# make a dict to store the weights in the weight list as keys...actual weights can be the keys and there values can be the
# indices where the weights are at in the list
# then i need to loop through the weights again and check to see if the limit - weight is a key in the dict
# if it is then that means i know the two weights who add up to the limit - the current weight and limit - weight weight
# i can then look those values up in the dict to get the indices of the two weights
# need to return the indices as a tuple with the greater index being first


def create_weight_dict(weights, length):
    weight_dict = {}
    for i, weight in enumerate(weights):
        if weight in weight_dict:
            weight_dict[weight] += [i]
        else:
            weight_dict[weight] = [i]
    return weight_dict

def get_indices_of_item_weights(weights, length, limit):
    weight_dict = create_weight_dict(weights, length)

    for weight in weights:
        dict_key = limit - weight
        if dict_key in weight_dict:
            weight_indices = []
            # if the there a multiple indices with the same weight in other words
            if len(weight_dict[dict_key]) > 1:
                weight_indices = weight_dict[dict_key]
                weight_indices.sort(reverse=True)
                print(weight_indices)
            else:
                weight1 = weight_dict[dict_key]
                weight2 = weight_dict[weight]
                weight_indices = weight1 + weight2
                weight_indices.sort(reverse=True)

            return tuple(weight_indices)

    return None
