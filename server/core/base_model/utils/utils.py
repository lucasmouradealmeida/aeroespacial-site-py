import re
import typing as t


def camel_to_snake(d: t.Dict[str, t.Any]) -> t.Dict[str, t.Any]:
    """Transforma chave do dicionario de camelCase para snake_case.

    Args:
        d (Dict[str, Any]): Dicionario que sera trabalhado.

    Returns:
        Dict[str, Any]: Dicionario com as chaves em snake_case.
    """
    regex_upper = re.compile(r"([A-Z0-9][a-z]*)")

    def value(v_: t.Any) -> t.Any:
        if isinstance(v_, dict):
            return camel_to_snake(v_)
        elif isinstance(v_, list):
            return [value(i) for i in v_]
        else:
            return v_

    def convert(k_: str) -> str:
        aw = [w for w in regex_upper.split(k_) if w.strip()]
        return "_".join(aw).lower()

    return dict([(convert(k), value(v)) for k, v in d.items()])


def snake_to_camel(d: t.Dict[str, t.Any]) -> t.Dict[str, t.Any]:
    """Transforma chave do dicionario de snake_case para camelCase.

    Args:
        d (Dict[str, Any]): Dicionario que sera trabalhado.

    Returns:
        Dict[str, Any]: Dicionario com as chaves em camelCase.
    """

    def value(v_: t.Any) -> t.Any:
        if isinstance(v_, dict):
            return snake_to_camel(v_)
        elif isinstance(v_, list):
            return [value(i) for i in v_]
        else:
            return v_

    def convert(k_: str) -> str:
        aw = [
            (w.lower().capitalize() if n > 0 else w.lower())
            for n, w in enumerate(k_.split("_"))
        ]
        return "".join(aw)

    return dict([(convert(k), value(v)) for k, v in d.items()])


def sort_dict(d: t.Dict[str, t.Any], reverse: bool = False) -> t.Dict[str, t.Any]:
    """Classifica as chaves do dicionario.

    Args:
        d (Dict[str, Any]): Dicionario que sera trabalhado.
        reverse (bool): Clasificar em ordem descrescente. Defaults to False.

    Returns:
        Dict[str, Any]: Dicionario com as chaves ordenadas.
    """
    return dict((k, d[k]) for k in sorted(d.keys(), reverse=reverse))


def to_camel(string: str) -> str:
    """Convert text to camel case.

    Args:
        string (str): text.

    Returns:
        str: Text camel case.
    """
    return "".join(
        word.capitalize() if n > 0 else word for n, word in enumerate(string.split("_"))
    )
