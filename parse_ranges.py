def parse_ranges(seq):
    for grouping in seq.split(","):
        if "-" in grouping:
            lower, upper = grouping.strip().split("-")
            if 'exit' in grouping:
                lower = upper = grouping.strip().split("-")[0]
        else:
            lower = upper = grouping.strip()

        lower = int(lower)
        upper = int(upper) + 1

        yield from range(lower, upper)


if __name__ == '__main__':
    for idx, r in enumerate(parse_ranges('0,1-2,4-4,8-10,11-11')):
        print(idx, r)

    print(list(parse_ranges('0,1-2,4-4,8-10,11-11')))
