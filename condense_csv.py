import csv
import io
from itertools import groupby
from textwrap import dedent


def read_csv_from_string(text):
    f = io.StringIO(text.strip())
    reader = csv.reader(f)
    return [t for t in reader if t]


def condense_csv(data, id_name=None):
    def key_func(x):
        return x[0]

    parsed_data = read_csv_from_string(data)
    if id_name is None:
        id_name = parsed_data.pop(0)[0]
    parsed_data = sorted(parsed_data, key=key_func)
    d = (
        [k, list(g)]
        for k, g in groupby(parsed_data, key=key_func)
    )
    results = []
    for idx, (k, g) in enumerate(d):
        row = {x[1]: x[2] for x in g}
        if idx == 0:
            results.append(",".join([id_name] + list(row.keys())))
        results.append(",".join([k] + list(row.values())))
    return "\n".join(results)


if __name__ == "__main__":
    t = dedent("""
            01,Artist,Otis Taylor
            01,Title,Ran So Hard the Sun Went Down
            01,Time,3:52
            02,Artist,Waylon Jennings
            02,Title,Honky Tonk Heroes (Like Me)
            02,"Time","3:29"
            03,Artist,David Allan Coe
            03,Title,"Willie, Waylon, And Me"
            03,Time,3:26
    """)

    r = condense_csv(t)
    print(r)
