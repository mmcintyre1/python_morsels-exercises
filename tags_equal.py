from html.parser import HTMLParser
import shlex


def split_tag(tag):
    split_tags = shlex.split(tag.lower()[1:-1])
    all_attributes = {}
    for tag_group in split_tags:
        attribute, _, value = tag_group.partition("=")
        if attribute not in all_attributes:
            all_attributes[attribute] = value
    return all_attributes


def tags_equal(first_tag, last_tag):
    return split_tag(first_tag) == split_tag(last_tag)


class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


if __name__ == '__main__':
    tag_1 = "<input value='hello there' value='ok'>"
    tag_2 = '<input value="hello there">'
    p = MyHTMLParser()
    p.feed(tag_1)
