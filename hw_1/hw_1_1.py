import sys

def nl(file) -> None:
    try:
        for i, line in enumerate(file, start=1):
            print(f"{i:6}  {line}", end='')
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

def main() -> None:
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r') as file:
                nl(file)
        except FileNotFoundError:
            print(f"File {sys.argv[1]} not found.", file=sys.stderr)
    else:
        nl(sys.stdin)

if __name__ == "__main__":
    main()
