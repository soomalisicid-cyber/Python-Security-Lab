
import time
from collections import deque
from datetime import datetime

MAX_REQUESTS = 3
WINDOW_SECONDS = 10
LOG_FILE = "lab.log"

request_times = deque()

def write_log(message):
    timestamp = datetime.now().isoformat(timespec="seconds")
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"{timestamp} - {message}\n")

def check_request():
    now = time.monotonic()

    while request_times and now - request_times[0] >= WINDOW_SECONDS:
        request_times.popleft()

    if len(request_times) >= MAX_REQUESTS:
        write_log("BLOCKED: request limit reached")
        return False

    request_times.append(now)
    write_log("ALLOWED: local test request")
    return True

def main():
    print("Python Security Lab")
    print("Local simulation only; no SMS messages are sent.")

    for number in range(1, 6):
        if check_request():
            print(f"Test {number}: ALLOWED")
        else:
            print(f"Test {number}: BLOCKED")

    print(f"Test complete. Review {LOG_FILE}")

if __name__ == "__main__":
    main()


