# Garden-Simulator

A didactically simple CLI application for Python beginners.

## How The Project Is Organized


The rules of the garden simulator live in `garden.py`. This file uses simple functions and core programming concepts. Most of the edits you have to perform in this file.

The command-line interface lives in `main.py`. It reads what commands the player types, splits them into words, and then uses `if/else` logic to decide what should happen.

The garden drawing code lives in `cli_view.py`. The `GardenPrinter` class turns the garden data into an ASCII grid that can be printed in the terminal.

The tests live in `test_garden.py`. They show what the garden is supposed to do and help check that the rules still work after changes.

## Installation

Open PowerShell in the project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pytest
```

## Run

```powershell
python main.py
```

## CLI Commands

- `show`
- `dig row col`
- `plant row col crop`
- `water row col`
- `day`
- `harvest row col`
- `help`
- `quit`

## Grid Display

The `show` command prints row and column indices.


Example:

```text
     0   1   2
  +---+---+---+
 0| . | o |   |
  +---+---+---+
 1|   |   |   |
  +---+---+---+
 2|   |   | R |
  +---+---+---+
```

The symbols in the grid mean:

- empty space: an empty cell
- `o`: a dug hole
- `.`: a planted seed
- `R`: a ripe crop that can be harvested

## Data Model

Each cell is a dictionary with:

- `state`: `"empty"`, `"hole"`, `"seed"`, `"ripe"`
- `crop`: `None` or string
- `water`: integer
- `days_as_seed`: integer

## Rules

- `dig` is only allowed on `empty` and changes state to `hole`
- `plant` is only allowed on `hole`, changes state to `seed`, sets `crop`, sets `water=0`, and sets `days_as_seed=0`
- `water` is only allowed on `seed`, and increases water up to `WATER_MAX`
- `day` affects all cells at once:
  - water decreases by 1
  - growth is deterministic:
    - a `seed` with enough water gains one qualifying day
    - after `RIPE_DAYS_FROM_SEED` qualifying days, `seed` becomes `ripe`
- `harvest` is only allowed on `ripe`, returns the crop name, and resets the cell to `empty`
- harvesting a `tomato` also appends a line to `harvests/tomato.txt`

## Tests

```powershell
pytest -q test_garden.py -vv
```
