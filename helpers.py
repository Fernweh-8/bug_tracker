import csv
import os
from constants import BASE_DIR


def write_to_csv(issues, header_columns=['title', 'description', 'user']):
    path = os.path.join(BASE_DIR, "issues.csv")
    with open(path, "w+") as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,
                                fieldnames=header_columns)
        writer.writeheader()
        for issue in issues:
            writer.write(issue.__dict__)
