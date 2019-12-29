"""
Bite 246. Test print / standard output
"""
import pytest
from workouts import print_workout_days


@pytest.mark.parametrize('str_input, expected',
                         [('upper', 'Mon, Thu'), 
                          ('lower', 'Tue, Fri'),
                          ('cardio', 'Wed'),
                          ('strength', 'No matching workout'),
                          ('', 'Mon, Tue, Wed, Thu, Fri')])
def test_print_workout_days(capsys, str_input, expected):
    print_workout_days(str_input)
    output = capsys.readouterr().out.strip() # capture readout
    assert output == expected
