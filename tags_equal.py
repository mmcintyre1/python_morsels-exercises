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


if __name__ == '__main__':
    print(tags_equal("<input value='hello there'>", '<input value="hello there">'))
