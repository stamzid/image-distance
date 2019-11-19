import os
import csv
import backend.outputs
from backend.config.settings import FIELDNAMES


class CSVProcessor:
    def read_csv(self, file_path):
        file_data = []
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            file_data = list(reader)

        csvfile.close()

        return file_data

    def read_csv_data(self, form_data):
        str_file_value = form_data.decode('utf-8')
        f = str_file_value.splitlines()
        reader = csv.DictReader(f)
        file_data = list(reader)

        return file_data


    def write_csv(self, file_name, rows):
        dirname = os.path.abspath(backend.__package__)
        output_file = os.path.join(dirname, 'outputs', file_name)

        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)

        csvfile.close()

        return output_file




