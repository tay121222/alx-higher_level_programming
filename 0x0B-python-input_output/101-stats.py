#!/usr/bin/python3
"""script that reads stdin"""


def print_stats(size, status_codes):
    """script that reads stdin line
    by line and computes metrics
    """

    print("Total file size:", size)
    for code in sorted(status_codes):
        print(code + ":", status_codes[code])


if __name__ == "__main__":
    import sys
    from collections import defaultdict

    total_file_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_file_size, status_code_counts)

            parts = line.strip().split()

            try:
                file_size = int(parts[-1])
                total_file_size += file_size
            except (IndexError, ValueError):
                pass

            try:
                status_code = parts[-2]
                if status_code in [
                        '200', '301', '400', '401', '403', '404', '405', '500'
                        ]:
                    status_code_counts[status_code] += 1
            except IndexError:
                pass

        print_stats(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_code_counts)
        raise
