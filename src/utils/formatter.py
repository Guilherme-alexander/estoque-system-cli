def print_table(headers, rows):
    col_widths = [len(h) for h in headers]

    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))

    def linha():
        print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")

    def linha_dados(row):
        print("| " + " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row)) + " |")

    linha()
    linha_dados(headers)
    linha()

    for row in rows:
        linha_dados(row)

    linha()