import time
import threading
import multiprocessing

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def measure_sync(n: int, num_runs: int) -> int:
    start_time = time.time()
    for _ in range(num_runs):
        fibonacci(n)
    end_time = time.time()
    return end_time - start_time

def measure_threads(n: int, num_runs: int) -> int:
    threads = []
    start_time = time.time()

    for _ in range(num_runs):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time

def measure_processes(n: int, num_runs: int) -> int:
    processes = []
    start_time = time.time()

    for _ in range(num_runs):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    return end_time - start_time

def main() -> None:
    n = 35
    num_runs = 10

    with open("compare_time.txt", "w") as f:
        sync_time = measure_sync(n, num_runs)
        f.write(f"Sync time: {sync_time:.3f}s\n")

        threads_time = measure_threads(n, num_runs)
        f.write(f"Threads time: {threads_time:.3f}s\n")

        processes_time = measure_processes(n, num_runs)
        f.write(f"Processes time: {processes_time:.3f}s\n")

if __name__ == '__main__':
    main()
