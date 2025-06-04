import pandas as pd
import os

def concat_tace_dfs(tace_path):
    """ Concatenates the individual Tace outputs into one big csv file """
    orig_tace_files = os.listdir(tace_path)
    all_data = list()
    for csv in orig_tace_files:
        if csv.endswith('Table.csv'):
            frame = pd.read_csv(os.path.join(tace_path, csv), sep=",", index_col=False)
            frame['filename'] = os.path.basename(csv)
            all_data.append(frame)

    all_df = pd.concat(all_data, ignore_index=True)

    return all_df

def get_edus_ordered(c_edus,a_edus):
    #First find lowest number
    if c_edus[0] < a_edus[0]:
        left = c_edus
        right = a_edus
    else:
        left = a_edus
        right = c_edus
    #Then get range
    left_range = [x for x in range(left[0],left[1]+1)]
    right_range = [x for x in range(right[0],right[1]+1)]

    span_length = (right_range[-1] - left_range[0]) + 1

    return span_length

def add_span_length(all_df):

    span_length_1 = list()
    for row_no in range(len(all_df)):
        try:
            span_length_1.append(get_edus_ordered([int(all_df['C1-A'][row_no]), int(all_df['C2-A'][row_no])],[int(all_df['A1-A'][row_no]), int(all_df['A2-A'][row_no])]))
        except ValueError:
            span_length_1.append(float("nan"))

    span_length_2 = list()
    for row_no in range(len(all_df)):
        try:
            span_length_2.append(get_edus_ordered([int(all_df['C1-B'][row_no]), int(all_df['C2-B'][row_no])],[int(all_df['A1-B'][row_no]), int(all_df['A2-B'][row_no])]))
        except ValueError:
            span_length_2.append(float("nan"))

    all_df['span_length_1_all'] = span_length_1
    all_df['span_length_2_all'] = span_length_2

    return all_df

def create_tace_df(tace_path):

    concat = concat_tace_dfs(tace_path)
    final = add_span_length(concat)

    return final
