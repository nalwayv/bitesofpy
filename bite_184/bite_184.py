""" 
Bite 184. Analyze some Bite stats data 
"""
from collections import Counter
from csv import DictReader, OrderedDict
from os import path
from typing import List


DATA = path.join(path.dirname(__file__), 'tmp', 'bite_output_log.csv')

class BiteStats:
    
    def _load_data(self, data) -> List[OrderedDict]:
        result = []
        with open(path.abspath(data)) as f:
            dr = DictReader(f)
            for row in dr:
                result.append(row)
        return result

    def __init__(self, data=DATA):
        self.rows: List[OrderedDict] = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len(set([row['bite'] for row in self.rows]))

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len(
            set([
                row['bite'] for row in self.rows if row['completed'] == 'True'
            ]))

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len(set([row['user'] for row in self.rows]))
        pass

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        return len(
            set([
                row['user'] for row in self.rows if row['completed'] == 'True'
            ]))

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        counter = Counter([row['bite'] for row in self.rows])
        return int(counter.most_common()[0][0])

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        user = Counter([
            row['user'] for row in self.rows if row['completed'] == 'True'
        ]).most_common()
        return user[0][0]
