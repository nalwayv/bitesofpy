""" 
Bite 223. Unix file permissions
"""


def get_octal_from_file_permission(rwx: str) -> str:
    """Receive a Unix file permission and convert it to
       its octal representation.

       In Unix you have user, group and other permissions,
       each can have read (r), write (w), and execute (x)
       permissions expressed by r, w and x.

       Each has a number:
       r = 4
       w = 2
       x = 1

       So this leads to the following input/ outputs examples:
       rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
       rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
       r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
    """
    fp = {'r': 4, 'w': 2, 'x': 1}
    res = []
    for v in [rwx[i:i + 3] for i in range(0, len(rwx), 3)]:
        res.append(str(sum([fp.get(x, 0) for x in v])))

    return ''.join(res)


if __name__ == "__main__":
    tests = [('-----x-w-', '012'), ('-----x-wx', '013'), ('-----xr--', '014'),
             ('-----xr-x', '015'), ('-----xrw-', '016'), ('-----xrwx', '017'),
             ('----w--wx', '023'), ('----w-r--', '024'), ('----w-r-x', '025'),
             ('----w-rw-', '026'), ('----w-rwx', '027'), ('----wxr--', '034'),
             ('----wxr-x', '035'), ('----wxrw-', '036'), ('----wxrwx', '037'),
             ('---r--r-x', '045'), ('---r--rw-', '046'), ('---r--rwx', '047'),
             ('---r-xrw-', '056'), ('---r-xrwx', '057'), ('---rw-rwx', '067'),
             ('--x-w--wx', '123'), ('--x-w-r--', '124'), ('--x-w-r-x', '125'),
             ('--x-w-rw-', '126'), ('--x-w-rwx', '127'), ('--x-wxr--', '134'),
             ('--x-wxr-x', '135'), ('--x-wxrw-', '136'), ('--x-wxrwx', '137'),
             ('--xr--r-x', '145'), ('--xr--rw-', '146'), ('--xr--rwx', '147'),
             ('--xr-xrw-', '156'), ('--xr-xrwx', '157'), ('--xrw-rwx', '167'),
             ('-w--wxr--', '234'), ('-w--wxr-x', '235'), ('-w--wxrw-', '236'),
             ('-w--wxrwx', '237'), ('-w-r--r-x', '245'), ('-w-r--rw-', '246'),
             ('-w-r--rwx', '247'), ('-w-r-xrw-', '256'), ('-w-r-xrwx', '257'),
             ('-w-rw-rwx', '267'), ('-wxr--r-x', '345'), ('-wxr--rw-', '346'),
             ('-wxr--rwx', '347'), ('-wxr-xrw-', '356'), ('-wxr-xrwx', '357'),
             ('-wxrw-rwx', '367'), ('r--r-xrw-', '456'), ('r--r-xrwx', '457'),
             ('r--rw-rwx', '467'), ('r-xrw-rwx', '567')]

    for arg, result in tests:
        ok = get_octal_from_file_permission(arg) == result
        print(ok)
