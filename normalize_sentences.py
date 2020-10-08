import re
from textwrap import dedent

SENTENCE_END_RE = re.compile(r'''
    (?<= [.?!] )            # A sentence ender before our space
    (?<! \. . \. )          # But no other dot before it (P.S., 5.5, etc)
    (?<! [A-Z][a-z]\. )     # And no 2-letter honorific before our space
    (?<! [A-Z][a-z]{2}\. )  # And no 3-letter honorific before our space
    \s                      # And then a single whitespace character
    (?= [A-Z] )             # And a capital letter
''', re.VERBOSE)


def normalize_sentences(sentences):
    return re.sub(SENTENCE_END_RE, r"  ", sentences)


def main():
    sentences = (
        "Do you know about the work of Dr. Rosalind Franklin? You can "
        "find out what she did by using google.com. Google is used by "
        "1.17 billion people (as of December 2012). That's a lot people!"
    )
    print(normalize_sentences(sentences))


if __name__ == "__main__":
    main()
