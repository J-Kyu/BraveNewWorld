import pandas as pd
import argparse
from IPython.display import display

if __name__ == '__main__':

    # parameter
    parser = argparse.ArgumentParser(description = "This is test Program")

    parser.add_argument('--f', type=str, default='./test.xlsx', help='Not ready yet')

    args = parser.parse_args()
    path = args.f

    rowPairList = dict()
    # reading xlsx
    # Start index start from any exisiting word grid
    # header: column
    # index: row
    try:
        excelFile = pd.read_excel(path,keep_default_na=False)
        for rowIndex  in range(len(excelFile)):
            for colIndex in range(len(excelFile.loc[rowIndex])):
                word = excelFile.loc[rowIndex][colIndex]
                if not word:
                    continue

                if colIndex not in rowPairList:
                    rowPairList[colIndex] = ['{}'.format(word)]
                else:
                    rowPairList[colIndex].append(word)
    except Exception as e:
        print(e)
    for key in rowPairList.keys():
        print("---------{}---------".format(rowPairList[key][0]))
        for i in range(1, len(rowPairList[key])):
            print(rowPairList[key][i])
    print("\n\n END")
