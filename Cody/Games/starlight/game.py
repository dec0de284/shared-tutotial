from lib.binary_reader import Reader
from pathlib import Path

path = Path("assets.bin").resolve()
asset_dict = Reader(path).read()

for dialogue in asset_dict["story"]["scene"]["prologue"]:
    input(dialogue)

prologue_choices = list(asset_dict["choices"]["prologue"].keys())

input_choice = None
while input_choice != "4":
    for dialogue in asset_dict["story"]["scene"]["free_roam_prologue"]:
        print(dialogue)
    for choice in prologue_choices:
        print(choice)
    input_choice = input("Choice (1-4): ")
    if input_choice.isdigit():
        if 0 < int(input_choice) < len(prologue_choices) + 1:
            for dialogue in asset_dict["choices"]["prologue"][prologue_choices[int(input_choice) - 1]]:
                input(dialogue)
        else:
            print("\033[91mError: Invalid input!\033[0m")

    else:
        print("\033[91mError: Invalid input!\033[0m")
