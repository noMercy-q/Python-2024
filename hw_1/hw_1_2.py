import sys

def tail_lines(file, num_lines: int) -> None:
    return file.readlines()[-num_lines:]

def main() -> None:
    FILE_LINES_COUNT = 10
    STDIN_LINES_COUNT = 17
    num_files = len(sys.argv) - 1
    
    if num_files == 0:
        result = tail_lines(sys.stdin, STDIN_LINES_COUNT)
        print(''.join(result), end='')
    else:
        for i, filename in enumerate(sys.argv[1:], 1):
            try:
                with open(filename, 'r') as file:
                    result = tail_lines(file, FILE_LINES_COUNT)

                if num_files > 1:
                    print(f"==> {filename} <==")
                print(''.join(result), end='')
                if i != num_files:
                    print()
            except FileNotFoundError:
                print(f"File '{filename}' not found", file=sys.stderr)

if __name__ == "__main__":
    main()
