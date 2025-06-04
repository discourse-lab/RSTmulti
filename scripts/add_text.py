import pandas as pd
import os
import re

def create_edu_dict(corpus_path):
    """ Creates a dictionary with each EDU for each file
        EDUs are in ascending order, starting at 1 """
    rst_files = os.listdir(corpus_path)
    all_edu_files = dict()
    for file in rst_files:
        if file.endswith(".rs3"):
            df_filename = "Comparison_" + file[:-4] + "_Table.csv"
            edu_file = dict()
            n = 0
            with open(corpus_path + file, "r", encoding="UTF-8") as input_file:
                for x in input_file.readlines():
                    if '<segment id=' in x:
                        n += 1
                        _edu = re.findall('>.*<', x)
                        _edu = _edu[0][1:-1]
                        edu_file[n] = _edu
                all_edu_files[df_filename] = edu_file

    return all_edu_files


def get_edu_text(c1,c2,a1,a2,filename,edu_dict):
    if c1 == "blank":
        return "blank", "blank"
    span1 = [x for x in range(int(c1), (int(c2)+1))]
    span2 = [x for x in range(int(a1), (int(a2)+1))]
    span1text = ""
    span2text = ""
    for edu in span1:
        try:
            span1text += edu_dict[filename][edu] + " "
        except KeyError:
            span1text += "PROBLEM WITH EDU PARSING "
    for edu in span2:
        try:
            span2text += edu_dict[filename][edu] + " "
        except KeyError:
            span2text += "PROBLEM WITH EDU PARSING "


    if c1 < a1:
        return span1text, span2text
    if c1 > a1:
        return span2text, span1text


def add_edu_text(input_df, corpus_path):
    edu_dict = create_edu_dict(corpus_path)
    input_df = input_df.fillna(value="blank")
    input_df[['Text1a','Text1b']] = pd.DataFrame(input_df.apply(lambda row: get_edu_text(row['C1-A'], row['C2-A'], row['A1-A'], row['A2-A'], row['filename'], edu_dict), axis=1).to_list())
    input_df[['Text2a','Text2b']] = pd.DataFrame(input_df.apply(lambda row: get_edu_text(row['C1-B'], row['C2-B'], row['A1-B'], row['A2-B'], row['filename'], edu_dict), axis=1).to_list())

    input_df.to_csv("tace_with_text.csv")
    return input_df
