import sys

def count_statistics(data: str) -> tuple[int, int, int]:
    lines = data.count('\n')
    words = len(data.split())
    bytes_count = len(data.encode('utf-8'))
    return lines, words, bytes_count

def process_file(filename: str) -> tuple[int, int, int]:
    with open(filename, 'r') as file:
        data = file.read()
    return count_statistics(data)

def process_stdin() -> tuple[int, int, int]:
    data = sys.stdin.read()
    return count_statistics(data)

def print_statistics(stats: tuple[int, int, int], precision: int, filename: str=None) -> None:
    lines, words, bytes_count = stats
    if filename:
        print(f"{lines:>{precision}} {words:>{precision}} {bytes_count:>{precision}} {filename}")
    else:
        print(f"{lines:>{precision}} {words:>{precision}} {bytes_count:>{precision}}")

def get_precision(stats_list: list[tuple[int, int, int]]) -> int:
    max_lines = max(stats[0] for stats in stats_list)
    max_words = max(stats[1] for stats in stats_list)
    max_bytes = max(stats[2] for stats in stats_list)
    
    return max(len(str(max_lines)), len(str(max_words)), len(str(max_bytes)))

def main() -> None:
    STDIN_PRECISION = 7

    total_lines, total_words, total_bytes = 0, 0, 0
    num_files = len(sys.argv) - 1
    stats_list: List[Tuple[int, int, int]] = []

    if num_files == 0:
        stats = process_stdin()
        print_statistics(stats, STDIN_PRECISION)
    else:
        for file in sys.argv[1:]:
            try:
                stats = process_file(file)
                stats_list.append(stats)
                total_lines += stats[0]
                total_words += stats[1]
                total_bytes += stats[2]
            except FileNotFoundError:
                print(f"File '{file}' not found", file=sys.stderr)
                return 1
        
        precision = get_precision(stats_list)
        
        for i, filename in enumerate(sys.argv[1:]):
            print_statistics(stats_list[i], precision, filename)
        
        if num_files > 1:
            total_stats = (total_lines, total_words, total_bytes)
            print_statistics(total_stats, precision, 'total')

if __name__ == "__main__":
    main()
