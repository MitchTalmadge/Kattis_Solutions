import sys
import bisect


def choose_cookie(cookies: list):
    """ Picks a cookie to send for packaging.
    Removes from list after selecting.
    :returns The cookie selected for packaging.
    """
    if len(cookies) % 2 == 0:
        cookie_index = int((len(cookies) / 2) + 1) - 1
    else:
        cookie_index = int((len(cookies) + 1) / 2) - 1

    cookie = cookies[cookie_index]
    del cookies[cookie_index]
    return cookie


cookies = []
for line in sys.stdin:
    if line[:1] == "#":
        # Send out a cookie
        print(choose_cookie(cookies))
    else:
        # Add a cookie to the list
        diam = int(line)
        bisect.insort(cookies, diam)
