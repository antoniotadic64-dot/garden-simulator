class GardenPrinter:
    SYMBOLS = {
        "empty": "",
        "hole": "o",
        "seed": ".",
        "ripe": "R",
    }

    def render(self, garden):
        if not garden:
            return "(empty garden)"

        cols = len(garden[0])
        cell_width = 3
        lines = []

        header = "   " + " ".join(f"{col:>{cell_width}}" for col in range(cols))
        lines.append(header)

        horizontal_line = "  +" + "+".join("-" * cell_width for _ in range(cols)) + "+"
        lines.append(horizontal_line)

        for row_index, row in enumerate(garden):
            chars = []
            for cell in row:
                chars.append(self.SYMBOLS.get(cell["state"], "?"))
            row_line = f"{row_index:>2}|"
            for char in chars:
                row_line += f"{char:^{cell_width}}|"
            lines.append(row_line)
            lines.append(horizontal_line)
        return "\n".join(lines)

    def print(self, garden):
        print(self.render(garden))
