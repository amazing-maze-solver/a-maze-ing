from rich.console import Console
from scripts.location_functions import sleep, import_data

# global
console = Console()


def main() -> None:
    location = import_data()
    console.print(location, style="bold green")
    location = location.transfer_maze_and_or_solution(location.locations.get("main"))

    while True:
        sleep(2)
        print("")
        if location.location == "good_bye":
            location.action()
            break
        location = location.action()


if __name__ == "__main__":
    main()
