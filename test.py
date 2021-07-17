import pandas as pd
import argparse


if __name__ == '__main__':

    # parameter
    parser = argparse.ArgumentParser(description = "This is test Program")

    parser.add_argument('--f', type=str, default='./test.xlsx', help='Not ready yet')

    args = parser.parse_args()
    path = args.f


    # reading xlsx
    try:
        excelFile = pd.read_excel(path,header=2,keep_default_na=False)
        print(excelFile)
        print(type(excelFile))
    except Exception as e:
        print(e)
