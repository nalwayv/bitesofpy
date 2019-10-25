"""
Bite 156: Make an index of story characters
"""
import re

CHARACTERS = [
    'Red Riding Hood', ('Grandmother', 'Grandma', 'Granny'), 'wolf', 'woodsman'
]
CHARACTERS2 = [
    'elder brother', 'younger brother', ('the tree', 'magical tree')
]

text = """
Once upon a time, there was a little girl who lived in a village near the forest.  Whenever she went out, the little girl wore a red riding cloak, so everyone in the village called her Little Red Riding Hood.
One morning, Little Red Riding Hood asked her mother if she could go to visit her grandmother as it had been awhile since they'd seen each other.
"That's a good idea," her mother said.  So they packed a nice basket for Little Red Riding Hood to take to her grandmother.
When the basket was ready, the little girl put on her red cloak and kissed her mother goodbye.
"Remember, go straight to Grandma's house," her mother cautioned.  "Don't dawdle along the way and please don't talk to strangers!  The woods are dangerous."
"Don't worry, mommy," said Little Red Riding Hood, "I'll be careful."
But when Little Red Riding Hood noticed some lovely flowers in the woods, she forgot her promise to her mother.  She picked a few, watched the butterflies flit about for awhile, listened to the frogs croaking and then picked a few more.
Little Red Riding Hood was enjoying the warm summer day so much, that she didn't notice a dark shadow approaching out of the forest behind her...
Suddenly, the wolf appeared beside her.
"What are you doing out here, little girl?" the wolf asked in a voice as friendly as he could muster.
"I'm on my way to see my Grandma who lives through the forest, near the brook,"  Little Red Riding Hood replied.
Then she realized how late she was and quickly excused herself, rushing down the path to her Grandma's house.
The wolf, in the meantime, took a shortcut...
The wolf, a little out of breath from running, arrived at Grandma's and knocked lightly at the door.
"Oh thank goodness dear!  Come in, come in!  I was worried sick that something had happened to you in the forest," said Grandma thinking that the knock was her granddaughter.
The wolf let himself in.  Poor Granny did not have time to say another word, before the wolf gobbled her up!
The wolf let out a satisfied burp, and then poked through Granny's wardrobe to find a nightgown that he liked.  He added a frilly sleeping cap, and for good measure, dabbed some of Granny's perfume behind his pointy ears.
A few minutes later, Red Riding Hood knocked on the door.  The wolf jumped into bed and pulled the covers over his nose.  "Who is it?" he called in a cackly voice.
"It's me, Little Red Riding Hood."
"Oh how lovely!  Do come in, my dear," croaked the wolf.
When Little Red Riding Hood entered the little cottage, she could scarcely recognize her Grandmother.
"Grandmother!  Your voice sounds so odd.  Is something the matter?" she asked.
"Oh, I just have touch of a cold," squeaked the wolf adding a cough at the end to prove the point.
"But Grandmother!  What big ears you have," said Little Red Riding Hood as she edged closer to the bed.
"The better to hear you with, my dear," replied the wolf.
"But Grandmother!  What big eyes you have," said Little Red Riding Hood.
"The better to see you with, my dear," replied the wolf.
"But Grandmother!  What big teeth you have," said Little Red Riding Hood her voice quivering slightly.
"The better to eat you with, my dear," roared the wolf and he leapt out of the bed and began to chase the little girl.
Almost too late, Little Red Riding Hood realized that the person in the bed was not her Grandmother, but a hungry wolf.
She ran across the room and through the door, shouting, "Help!  Wolf!" as loudly as she could.
A woodsman who was chopping logs nearby heard her cry and ran towards the cottage as fast as he could.
He grabbed the wolf and made him spit out the poor Grandmother who was a bit frazzled by the whole experience, but still in one piece."Oh Grandma, I was so scared!"  sobbed Little Red Riding Hood, "I'll never speak to strangers or dawdle in the forest again."
"There, there, child.  You've learned an important lesson.  Thank goodness you shouted loud enough for this kind woodsman to hear you!"
The woodsman knocked out the wolf and carried him deep into the forest where he wouldn't bother people any longer.
Little Red Riding Hood and her Grandmother had a nice lunch and a long chat.
"""

text2 = """
There were once two brothers who lived on the edge of a forest.
The elder brother was very mean to his younger brother and ate up all the food and took all his good clothes.
One day, the elder brother went into the forest to find some firewood to sell in the market.
As he went around chopping the branches of a tree after tree, he came upon a magical tree.
The tree said to him, ‘Oh kind sir, please do not cut my branches.
If you spare me, I will give you my golden apples’.
The elder brother agreed but was disappointed with the number apples the tree gave him.
Greed overcame him, and he threatened to cut the entire trunk if the tree didn’t give him more apples.
The magical tree instead showered upon the elder brother hundreds upon hundreds of tiny needles.
The elder brother lay on the ground crying in pain as the sun began to lower down the horizon.
The younger brother grew worried and went in search of his elder brother.
He found him with hundreds of needles on his skin.
He rushed to his brother and removed each needle with painstaking love.
After he finished, the elder brother apologised for treating him badly and promised to be better.
The tree saw the change in the elder brother’s heart and gave them all the golden apples they could ever need.
"""


def make_character_index(text=text, characters=CHARACTERS):
    """Return a dict with keys are characters (lowercased) and values
       the lines they appear in sorted order.
       Matches should be case insensitive.
       If a character has multiple synonyms
       - e.g. ('Grandmother', 'Grandma', 'Granny') -
       then return the former as key.
    """
    indexes = {}
    for key in characters:
        if isinstance(key, tuple):
            pattern = "|".join([k.lower() for k in key])
            nums = []
            for idx, line in enumerate(text.splitlines()):
                match = re.findall(f"{pattern}", line.lower())
                if match:
                    nums.append(idx)
            indexes[key[0].lower()] = nums
        else:
            nums = []
            for idx, line in enumerate(text.splitlines()):
                match = re.findall(key.lower(), line.lower())
                if match:
                    nums.append(idx)
            indexes[key.lower()] = nums
    return indexes


if __name__ == "__main__":
    keys = ('elder brother', 'younger brother', 'the tree')
    values = (
        [2, 3, 7, 9, 10, 11, 14, 15],
        [2, 11],
        [4, 5, 7, 8, 9, 15],
    )
    actual = make_character_index(text2, CHARACTERS2)
    expected = dict(zip(keys, values))
    if actual == expected:
        print("passed")

    keys = ('red riding hood', 'grandmother', 'wolf', 'woodsman')
    values = (
        [1, 2, 3, 6, 7, 8, 11, 18, 19, 21, 24, 26, 28, 30, 33, 36], 
        [2, 3, 5, 11, 12, 14, 15, 16, 17, 21, 22, 24, 26, 28, 30, 33, 36], 
        [9, 10, 13, 14, 16, 17, 18, 20, 23, 25, 27, 29, 30, 31, 33, 35], 
        [32, 34, 35])
    expected = dict(zip(keys, values))
    actual = make_character_index(text, CHARACTERS)
    if actual == expected:
        print("passed")