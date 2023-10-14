import re
import unicodedata


def text_normalize(text: str) -> str:
    text_enc = text.encode("utf-8", "ignore").decode("utf-8", "ignore")
    char_list = []
    for c in text_enc:
        if c in ["\n", "\t"] or c.isprintable():
            char_list.append(c)
    text_new = "".join(char_list)
    return text_new


def replace_latin_characters(text: str) -> str:
    text_new = unicode_normalize(text)
    text_new = text_new.encode("ASCII", "ignore").decode("ASCII", "ignore")
    return text_new


def unicode_normalize(text: str) -> str:
    text_new = text.encode("unicode-escape", "ignore").decode(
        "unicode-escape", "ignore"
    )
    text_new = unicodedata.normalize("NFKD", text_new)
    return text_new


def remove_tab_newline(text: str) -> str:
    textnew = re.sub(r"\n|\r|\t", " ", text)
    return textnew
