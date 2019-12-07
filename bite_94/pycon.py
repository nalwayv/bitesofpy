""" 
Bite 94. Parse PyCon talk data from YouTube
"""
import os
import pickle
import re
from collections import namedtuple
from typing import List

# import urllib.request

# prework
# download pickle file and store it in a tmp file
pkl_file = 'pycon_videos.pkl'
data = 'http://projects.bobbelderbos.com/pcc/{}'.format(pkl_file)
pycon_videos = os.path.join(os.path.dirname(__file__), 'tmp', pkl_file)
# urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = namedtuple('Video', 'id title duration metrics')


def load_pycon_data(pycon_videos: str):
    """Load the pickle file (pycon_videos) and return the data structure
       it holds
    """
    p_data = None
    with open(pycon_videos, 'rb') as pickle_file:
        p_data = pickle.load(pickle_file)
    return p_data


# Helpers
def get_vid_stat(vid: Video, category) -> int:
    """get_vid_stat
    """
    metrics: dict = vid.metrics
    value: str = metrics.get(category)

    if value:
        return int(value)
    return 0


def get_ratio(vid: Video) -> float:
    """get ratio
    """
    views = get_vid_stat(vid, 'viewCount')
    likes = get_vid_stat(vid, 'likeCount')
    dislikes = get_vid_stat(vid, 'dislikeCount')
    return round(((likes - dislikes) / views) * 100, 2)


def get_minutes(video: Video) -> int:
    """get min for over under 24 min
    """
    mins = re.findall(r'PT(\d+)M', video.duration)
    if mins:
        return int(mins[0])
    return 1000


def get_hours(video: Video) -> int:
    hours = re.findall(r'PT(\d+)H', video.duration)
    if hours:
        return int(hours[0])
    return 0


def get_most_popular_talks_by_views(videos: list) -> List[Video]:
    """Return the pycon video list sorted by viewCount
    """
    return sorted(videos,
                  key=lambda vid: get_vid_stat(vid, 'viewCount'),
                  reverse=True)


def get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list
    """
    return sorted(videos, key=get_ratio, reverse=True)


def get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""
    return [v for v in videos if get_hours(v) >= 1]


def get_talks_lt_twentyfour_min(videos: List[Video]):
    """Filter videos list down to videos that have a duration of less than
       24 minutes
    """
    return [v for v in videos if get_minutes(v) < 24]
