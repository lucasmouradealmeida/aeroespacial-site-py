import base64
import json
import re
import unicodedata
from typing import Any, Optional

from pydash import py_


def replace_tags(text: str, fields: dict, default_value: str = "") -> str:
    """
    Substituir tags no texto pelos campos recebidos.
    Parameters
    ----------
    text: string
        Texto com tags. Ex.: "Meu nome é {{nome}}"
    fields: dict
        Campos que irão substituir as tags. Ex: { nome: 'Joao' }
    default_value: str
        Caso o campo não exista, atribuir o valor preenchido
    Returns
    -------
    string
        Texto com as tags substituidas.
    """
    # Constantes
    REGEX_FIND_TAGS = re.compile(r"(?<=\{\{)(\s*\w+\s*)(?=\}\})")
    REGEX_REPLACE_TAGS = r"(\{\{\s*)(%s)(\s*\}\})"
    # Validacao de campos
    if not text or not fields or not py_.is_string(text) or not py_.is_dict(fields):
        return ""
    # Extrair tags
    text_tags = REGEX_FIND_TAGS.findall(text)
    # Remover espaços
    tags_cleaned = list(map(lambda t: t.replace(" ", ""), text_tags))
    # Classificar
    tags_sorted = sorted(tags_cleaned)
    # Remoção de duplicidade
    tags_uniq = py_.uniq(tags_sorted)
    # Texto que será substituido
    text_final = text
    # Substituir
    for tag in tags_uniq:
        regex = REGEX_REPLACE_TAGS % tag
        text_final = re.sub(
            re.compile(regex), str(py_.get(fields, tag, default_value)), str(text_final)
        )
    # Retorno
    return text_final


def interpolation(
    text: Optional[str] = None,
    fields: Optional[dict[Any, Any]] = None,
    is_json: bool = False,
) -> str:
    """
    Executa a substituição de tags (Ex.: "{{campo}}") dentro do texto a partir de
      um dicionario.
    :param text: Texto com tags para serem substituidas.
    :type text: str
    :param fields: Dicionario com campos para substituição. (Opcional)
    :type fields: dict
    :param is_json: É um json. Se sim, preencher com True. Default: False.
    :type is_json: bool
    :return: Retorna texto com a interpolação dos campos feita.
    :rtype: str
    """

    def parse_field(value, is_js: bool) -> str:
        return json.dumps(value, default=str) if is_js else str(value)

    if not isinstance(text, str):
        return ""
    fields = fields if isinstance(fields, dict) else dict()
    is_json = is_json if isinstance(is_json, bool) else False
    novo_texto = text
    for campo in re.findall(r"{{\s*(\w+)\s*}}", text, re.IGNORECASE):
        novo_texto = re.sub(
            (r"{{\s*" + campo + r"\s*}}"),
            parse_field(fields.get(campo, None), is_json),
            novo_texto,
        )
    return novo_texto


def get_only_numbers(text: str = "") -> str:
    """
    Função para remover caracters que não são numericos.
    Parameters
    ----------
    text: str
        Campos de texto que contem os numeros.
    Returns
    -------
    str
        Retorna apenas os numeros
    """
    if not isinstance(text, str):
        return ""
    numbers = "".join(re.findall(r"\d+", text))
    return numbers


def remove_tab_newline(text: str) -> str:
    """
    Remover caracteres de tabulações e novas linhas.
    Parameters
    ----------
    text: str
        Texto que sera removido as linhas e tabulações
    Returns
    -------
    str
        Texto com a limpeza do codigo
    """
    if not isinstance(text, str):
        return ""
    textnew = re.sub(r"\n|\r", " ", text)
    textnew = re.sub(r"\t", " ", textnew)
    return textnew


def remove_multiples_spaces(text: str) -> str:
    """
    Remover excesso de espaço no texto.
    Parameters
    ----------
    text: str
        Texto que será removido o excesso de espaços.
    Returns
    -------
    str
        Texto novo.
    """
    if not isinstance(text, str):
        return ""
    textnew = re.sub(r"\s{2,}", " ", text)
    return textnew


def clean_all(text: str) -> str:
    """
    Higienizador de texto.
    Parameters
    ----------
    text: str
        Texto que será higienizado.
    Returns
    -------
    str
        Texto higienizado.
    """
    if not isinstance(text, str):
        return ""
    textnew = remove_tab_newline(text)
    textnew = remove_multiples_spaces(textnew)
    return textnew


def text_normalize(text: str) -> str:
    """
    Normalizador de texto.
    Parameters
    ----------
    text: str
        Texto.
    Returns
    -------
    str
        Texto normalizado.
    """
    if not isinstance(text, str):
        return ""
    text_enc = text.encode("utf-8", "ignore").decode("utf-8", "ignore")
    char_list = []
    for c in text_enc:
        if c in ["\n", "\t"] or c.isprintable():
            char_list.append(c)
    text_new = "".join(char_list)
    return text_new


def replace_latin_characters(text: str) -> str:
    """
    Substituir caracteres latin (cedilha, acentos, etc...).
    Parameters
    ----------
    text: str
    Returns
    -------
    str
    """
    if not isinstance(text, str):
        return ""
    text_new = unicode_normalize(text)
    text_new = text_new.encode("ASCII", "ignore").decode("ASCII", "ignore")
    return text_new


def unicode_normalize(text: str) -> str:
    """
    Normalização via unicode.
    Parameters
    ----------
    text: str
    Returns
    -------
    str
    """
    if not isinstance(text, str):
        return ""
    text_new = text.encode("unicode-escape", "ignore").decode(
        "unicode-escape", "ignore"
    )
    text_new = unicodedata.normalize("NFKD", text_new)
    return text_new


def search_text(
    words: str,
    text: str,
    case_sensitive: bool = True,
    no_latin: bool = False,
    ignore_spaces: bool = False,
) -> bool:
    """
    Pesquisa de palavras dentro de textos
    Parameters
    ----------
    words: str
        Palavra(s) para serem pesquisadas.
    text: str
        Texto onde será pesquisado.
    case_sensitive: bool
        Respeitar caracteres maiusculos e minusculos.
        Default: True
    no_latin: bool
        Remover caracteres do enconde latin
        Default: False
    ignore_spaces: bool
        Desconsiderar excesso de espaços.
        Default: False
    Returns
    -------
    bool
        True = Encontrou
        False = Não encontrou
    """
    if not isinstance(words, str):
        return False
    if not isinstance(text, str):
        return False
    text1 = unicode_normalize(words)
    text2 = unicode_normalize(text)
    if no_latin:
        text1 = replace_latin_characters(text1)
        text2 = replace_latin_characters(text2)
    text1 = re.escape(text1)
    if ignore_spaces:
        text1 = re.sub(r"(\\\s)+", r"\s+", text1)
    if not case_sensitive:
        text1 = f"(?i){text1}"
    result = bool(re.search(text1, text2))
    return result


def b64encode(texto: str) -> str:
    """
    Transformar texto em base64
    :param texto: Texto para transformar.
    :type texto: str
    :return: texto em base64
    :rtype: str
    """
    if not isinstance(texto, str):
        return str()
    return base64.urlsafe_b64encode(texto.encode("UTF-8")).decode("ascii")


def clean_spaces(txt: str) -> str:
    """Remove excesso de espaços.

    Args:
        txt (str): texto que será higienizado.

    Returns:
        str: texto com quantidade de espaços reduzidos.
    """
    return re.sub(r"\s{2,}", " ", txt)
