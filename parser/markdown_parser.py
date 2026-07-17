import hashlib


def generate_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def clean_heading(text):

    text = text.replace("*", "")

    text = text.replace("`", "")

    text = text.strip()

    return text


def parse_markdown(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    nodes = []

    stack = []

    current_heading = None

    current_level = None

    current_body = []

    for line in lines:

        line = line.rstrip()

        # Heading
        if line.startswith("#"):

            if current_heading:

                body = "\n".join(current_body).strip()

                parent = None

                while stack and stack[-1]["level"] >= current_level:
                    stack.pop()

                if stack:
                    parent = stack[-1]["heading"]

                node = {

                    "heading": current_heading,

                    "level": current_level,

                    "body": body,

                    "parent": parent,

                    "content_hash": generate_hash(body)

                }

                nodes.append(node)

                stack.append(node)

            current_level = len(line.split(" ")[0])

            heading = line.lstrip("#")

            heading = clean_heading(heading)

            if heading == "":

                current_heading = None

                current_body = []

                continue

            current_heading = heading

            current_body = []

        else:

            # Keep lists, tables and paragraphs exactly as they are.
            current_body.append(line)

    if current_heading:

        body = "\n".join(current_body).strip()

        parent = None

        while stack and stack[-1]["level"] >= current_level:
            stack.pop()

        if stack:
            parent = stack[-1]["heading"]

        nodes.append({

            "heading": current_heading,

            "level": current_level,

            "body": body,

            "parent": parent,

            "content_hash": generate_hash(body)

        })

    return nodes