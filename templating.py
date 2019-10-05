import os
import re

templates = {}

def load_error(line, message):
    print("ERROR: {}, line {}".format(message, line))

def load_template(source):
    global templates

    # Bracket matching expression
    exp = '{%\s*(\w+)(?:\s+(\w+))?\s*%}'
    bstack = []
    new_tags = {}

    # Validate tags
    with open(source, 'r') as dom:
        for idx, line in enumerate(dom):
            m = re.search(exp, line)
            if not m is None:
                if m.group(1) == 'begin':
                    bstack.insert(0, m.group(2))
                elif m.group(1) == 'end':
                    if len(bstack == 0):
                        load_error(idx, "")
                    else:
                        bstack.pop()

    # Valid file parsing, update templates
    if len(bstack) == 0:
        templates.update(new_tags)
        print(templates)
    else:
        print("ERROR: Could not parse")

load_template("index.html")

'''
Template formatting:

{% being navigation %}
    <!-- some html code -->
{% end %}

'''