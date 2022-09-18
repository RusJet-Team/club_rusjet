import re


def get_current_link(link):
    pattern = r"((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)"
    result = re.findall(pattern, link)
    if result:
        link_id = result[-1][-1]
        current_lint = f"https://youtube.com/embed/{link_id}"
        return current_lint
    return link
