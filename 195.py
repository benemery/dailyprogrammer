"""
(Easy): Symbolic Link Resolution

http://www.reddit.com/r/dailyprogrammer/comments/2qmz12/20141228_challenge_195_easy_symbolic_link/
"""

def resolve_path(links, path):
    """Take list of "name:destination" symlink pairs and a path to resolve"""
    # Let's parse our links
    fs = {}
    for data in links:
        link, destination = data.split(':')
        # Folders paths can (but don't have to) end with a trailling /
        # To make our lives easier, remove all trailling slashes
        link = link.rstrip('/')
        destination = destination.rstrip('/')
        fs[link] = destination

    def follow_links(path, fs):
        if path not in fs:
            return path
        path = fs[path]
        return follow_links(path, fs)

    resolved_path = ""
    for chunk in path.split('/'):
        resolved_path = follow_links(resolved_path + chunk, fs)
        resolved_path += '/'

    if not path.endswith('/'):
        # Request path didn't have a final slash, so nor shall we
        resolved_path = resolved_path.rstrip('/')

    return resolved_path


if __name__ == '__main__':
    tests_inputs = [
            ("""4
/bin/thing:/bin/thing-3
/bin/thing-3:/bin/thing-3.2
/bin/thing-3.2/include:/usr/include
/usr/include/SDL:/usr/local/include/SDL
/bin/thing/include/SDL/stan""",
            "/usr/local/include/SDL/stan"),
            ("""1
/home/elite/documents:/media/mmcstick/docs
/home/elite/documents/office""",
            "/media/mmcstick/docs/office"),
            ("""3
/bin:/usr/bin
/usr/bin:/usr/local/bin/
/usr/local/bin/log:/var/log-2014
/bin/log/rc""",
            "/var/log-2014/rc"),
            ("""2
/etc:/tmp/etc
/tmp/etc/:/etc/
/etc/modprobe.d/config/""",
            None),
    ]

    for data, result in tests_inputs:
        lines = data.split('\n')
        n = int(lines[0])
        links = lines[1:n+1]
        path = lines[-1]

        try:
            res = resolve_path(links, path)
        except RuntimeError:
            res = None
            if result:
                # A result is expected, re raise
                raise
        assert res == result
