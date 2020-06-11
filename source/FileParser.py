import argparse
import csv
import pandas as pd  # pandas.read_csv


class FileParser:
    @staticmethod
    def ParseCLI():
        options = argparse.ArgumentParser()
        options.add_argument('-f', '--file', type=str, required=True)
        args = options.parse_args()

        # can be used like python main.py -f file
        # args.file
        data = pd.read_csv(args.file)

    @staticmethod
    def GetMagnitudeTime(data:pd.DataFrame):
        magnitude = data['mag']
        date = data['time']

    @staticmethod
    def Read4File(_file: str) -> pd.DataFrame:
        data: pd.DataFrame = pd.read_csv(_file)
        return data
