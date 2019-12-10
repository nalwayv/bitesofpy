""" 
Bite 198. Calculate my Mac's longest uptime
"""
from typing import List, Optional, Tuple
from datetime import datetime, timedelta
from dateutil.parser import parse
import re

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""

MAC2 = """
reboot ~ Tue Sep 22 12:52
reboot ~ Sun Aug 30 23:17
reboot ~ Sat Aug 29 01:12
reboot ~ Fri Aug 28 22:07
"""

MAC3 = """
reboot    ~                         Fri Dec 18 23:58
reboot    ~                         Mon Dec 14 09:54
reboot    ~                         Wed Dec 11 23:21
reboot    ~                         Tue Nov 17 21:52
reboot    ~                         Tue Nov 17 06:01
reboot    ~                         Wed Nov 11 12:14
reboot    ~                         Sat Oct 31 13:40
reboot    ~                         Wed Oct 28 15:56
reboot    ~                         Wed Oct 28 11:35
reboot    ~                         Tue Oct 27 00:00
reboot    ~                         Sun Oct 18 17:28
reboot    ~                         Sun Oct 18 17:11
reboot    ~                         Mon Oct  5 09:35
reboot    ~                         Sat Oct  3 18:57
"""


def get_times(reboot_str: str) -> Optional[List[datetime]]:
    pattern = r'~\s+(\w.*)'
    check = re.compile(pattern, re.MULTILINE)
    times = check.findall(reboot_str)

    if times:
        return [parse(time) for time in times]

    return None


def calc_max_uptime(reboots) -> Optional[Tuple[int, str]]:
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    times = get_times(reboots)
    if not times:
        return None

    n = len(times)
    res = []

    for i in range(1, n):
        t1 = times[i - 1]
        t2 = times[i]
        t3 = t1 - t2
        res.append((t3.days, t1.strftime('%Y-%m-%d')))

    return max(res, key=lambda x: x[0])


if __name__ == "__main__":
    print(calc_max_uptime(MAC1))
    print(calc_max_uptime(MAC2))
    print(calc_max_uptime(MAC3))