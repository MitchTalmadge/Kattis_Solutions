import sys


def choose_cookie(cookies: list):
    """ Picks a cookie to send for packaging.
    Sorts list, then removes from list after selecting.
    :returns The cookie selected for packaging.
    """
    cookies.sort()

    if len(cookies) % 2 == 0:
        cookie = cookies[int((len(cookies) / 2) + 1) - 1]
    else:
        cookie = cookies[int((len(cookies) + 1) / 2) - 1]

    cookies.remove(cookie)
    return cookie


cookies = []
for line in sys.stdin:
    if line[:1] == "#":
        # Send out a cookie
        print(choose_cookie(cookies))
    else:
        # Add a cookie to the list
        diam = int(line)
        cookies.append(diam)
