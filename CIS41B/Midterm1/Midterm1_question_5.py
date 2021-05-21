import pandas as pd


def dict_to_data_frame_with_key_index(de_dict):
    df = pd.DataFrame(data=de_dict, index=[0])
    return df


def dict_to_data_frame_with_value_index(de_dict):
    df = pd.DataFrame(data=de_dict, index=[1])
    return df


if __name__ == "__main__":

    d = {'Cat': 2, 'Dog': 3, 'Bird': 4, 'Fish': 6, 'Elephant': 5 }
    data_frame_with_key_index = dict_to_data_frame_with_key_index(d)
    print(data_frame_with_key_index)
    data_frame_with_value_index = dict_to_data_frame_with_value_index(d)
    print(data_frame_with_value_index)


"""
/Users/jakkus/PycharmProjects/CIS41B/venv/bin/python /Users/jakkus/PycharmProjects/CIS41B/CIS41B_FALL_2020_MIDTERM1.py
   Cat  Dog  Bird  Fish  Elephant
0    2    3     4     6         5
   Cat  Dog  Bird  Fish  Elephant
1    2    3     4     6         5

Process finished with exit code 0
"""