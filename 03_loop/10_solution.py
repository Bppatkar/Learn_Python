# exponential backoff strategy


import time

wait_time = 1
max_attempt = 5
attempt = 0

while attempt < max_attempt:
    print(
        "Attempt ",
        attempt + 1,
        "- wait time",
        wait_time,
    )
    wait_time *= 2
    attempt += 1
