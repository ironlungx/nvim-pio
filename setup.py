import glob
import os
from typing import TypeVar, Sequence, Optional

T = TypeVar("T")


def menu(options: Sequence[T], prompt: str, header: str) -> Optional[T]:
    print(header)
    for i, option in enumerate(options):
        print(f"{i+1}. {os.path.basename(option)}")  # Show just the framework name
    while True:
        try:
            c = int(input(f"{prompt} > "))
            if 1 <= c <= len(options):
                return options[c - 1]
            else:
                print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return None


def main():
    base_path = os.path.expanduser("~/.platformio/packages/")
    framework_dirs = glob.glob(os.path.join(base_path, "framework*"))
    framework_dirs = sorted([d for d in framework_dirs if os.path.isdir(d)])

    framework = menu(framework_dirs, "Select framework", "Available frameworks:")

    if framework:
        framework_name = os.path.basename(framework)
        with open(".framework", "w") as f:
            f.write(framework_name)
        print(f"Framework set to: {framework_name}")


if __name__ == "__main__":
    main()
