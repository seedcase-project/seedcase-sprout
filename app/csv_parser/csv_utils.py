import csv
import sys
from typing import IO
from app.csv_parser import CsvColumnStats


def derive_csv_column_types(file: IO, max_row_count: int = sys.maxsize):
    csv_reader = csv.reader(file)
    column_names = next(csv_reader)
    columns = [CsvColumnStats(column_name) for column_name in column_names]

    for row in csv_reader:
        # Return if max row_count is reached
        if columns[0].row_count >= max_row_count:
            return columns

        for i in range(len(columns)):
            columns[i].analyze(row[i])

    return columns
