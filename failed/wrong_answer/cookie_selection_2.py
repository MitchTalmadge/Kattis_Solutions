import sys
from queue import PriorityQueue


def choose_cookie(min_cookies: PriorityQueue, max_cookies: PriorityQueue):
    diam = min_cookies.get()[1]
    if len(min_cookies.queue) != len(max_cookies.queue):
        max_diam = max_cookies.get()
        min_cookies.put((-max_diam, max_diam))
    return diam


def add_cookie(diameter: int, min_cookies: PriorityQueue, max_cookies: PriorityQueue):
    if len(min_cookies.queue) != 0 and diameter > min_cookies.queue[0][1]:
        min_cookies.put((-diameter, diameter))
        if len(min_cookies.queue) > len(max_cookies.queue) + 1:
            max_cookies.put(min_cookies.get()[1])
    else:
        max_cookies.put(diameter)
        if len(max_cookies.queue) > len(min_cookies.queue):
            max_diam = max_cookies.get()
            min_cookies.put((-max_diam, max_diam))


def main():
    min_cookies = PriorityQueue()
    max_cookies = PriorityQueue()

    for line in sys.stdin:
        if line[:1] == "#":
            # Send out a cookie
            print(choose_cookie(min_cookies, max_cookies))
        else:
            # Add a cookie to the list
            diam = int(line)
            add_cookie(diam, min_cookies, max_cookies)


main()
