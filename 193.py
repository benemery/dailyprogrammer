"""
(Easy): Acronym Expander

http://www.reddit.com/r/dailyprogrammer/comments/2ptrmp/20141219_challenge_193_easy_acronym_expander/
"""
import re

ACRONYMS = (
    ("lol", "laugh out loud"),
    ("dw", "don't worry"),
    ("hf", "have fun"),
    ("gg", "good game"),
    ("brb", "be right back"),
    ("g2g", "got to go"),
    ("wtf", "what the fuck"),
    ("wp", "well played"),
    ("gl", "good luck"),
    ("imo", "in my opinion"),
)


def expand_words(line):
    """Take a line and expand it."""
    for acronym, text in ACRONYMS:
        # String matching, let's use some regex.
        # replace any match that is surrounded by 0 or 1 non text character
        line = re.sub(r'(\W{,1})%s(\W{,1})' % acronym, r'\1%s\2' % text, line)
    return line

if __name__ == '__main__':
    tests = [
        ('wtf that was unfair', 'what the fuck that was unfair'),
        ('gl all hf', 'good luck all have fun'),
    ]

    for test, expected in tests:
        assert expand_words(test) == expected
    
    # Now print the final example
    print expand_words("imo that was wp. Anyway I've g2g")
