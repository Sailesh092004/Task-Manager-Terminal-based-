import psutil
import time


def display_processes():
    processes = []
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        processes.append({
            'PID': process.info['pid'],
            'Name': process.info['name'],
            'CPU%': process.info['cpu_percent'],
            'Memory (MB)': process.info['memory_info'].rss / (1024 * 1024)
        })

    processes.sort(key=lambda x: x['CPU%'], reverse=True)

    return processes


def main():
    while True:
        print("\n===== Task Manager =====")
        print("PID    | Name                        | CPU%   | Memory (MB)")
        print("=" * 60)

        processes = display_processes()
        for process in processes:
            print(f"{process['PID']:<7}| {process['Name']:<28}| {process['CPU%']:.2f}| {process['Memory (MB)']:.2f}")

        action = input("\nOptions: 'q' to quit, 'r' to refresh: ")

        if action == 'q':
            break
        elif action == 'r':
            time.sleep(10)  # Sleep for 1 second before refreshing


if __name__ == "__main__":
    main()
