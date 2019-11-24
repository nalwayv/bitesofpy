"""
Bite 85. Write an advanced property
"""

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))

CONGRATS_MSG = ('Congrats, you earned {score} points '
                'obtaining the PyBites Ninja {rank} Belt')

NEW_SCORE_MSG = 'Set new score to {score}'


class NinjaBelt:
    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        belt_score = 0
        p = 0
        for s in scores:
            if new_score >= p and new_score < s:
                belt_score = p
            else:
                p = s
        return BELTS.get(belt_score)

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError('not an int')

        self._score = new_score

        belt = self._get_belt(new_score)
        
        if belt is not None:    
            if self._last_earned_belt == belt:
                # same
                print(NEW_SCORE_MSG.format(score=new_score))
            else:
                # update
                self._last_earned_belt = belt
                print(
                    CONGRATS_MSG.format(score=new_score,
                                        rank=belt.capitalize()))
        else:
            print(NEW_SCORE_MSG.format(score=new_score))

    score = property(_get_score, _set_score)


if __name__ == "__main__":
    nb = NinjaBelt()
    nb.score = 1
    nb.score = 20
    nb.score = 49
    nb.score = 50
    nb.score = 177
    print(nb._last_earned_belt)
