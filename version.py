from version_functools import to_list, equalize_lengths
from exceptions import ComparisonError
import functools


@functools.total_ordering
class Version:

    AUTHORITY_DICT = {
        "dev": 1, "alpha": 2, "a": 2, "beta": 3,
        "b": 3, "RC": 4, "rc": 4, "#": 5, "pl": 6,
        "p": 6
    }

    def __init__(self, version: str):
        self.version = version if isinstance(version, str) else None
        self.version_list = to_list(version)[::-1]

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.version_list == other.version_list
        else:
            raise ComparisonError("Impossible to compare version with non-version object")

    def __lt__(self, other):
        if isinstance(other, Version):
            self.version_list, other.version_list = equalize_lengths(self.version_list, other.version_list)
            return Version.lt_compare(self.version_list, other.version_list)
        else:
            raise ComparisonError("Impossible to compare version with non-version object")

    @staticmethod
    def lt_compare(lst_1: list, lst_2: list) -> bool:
        result_flag = bool()

        def lt_authority_compare(str_1: str, str_2: str):
            nonlocal result_flag
            authority_list = []
            for key in [str_1, str_2]:
                try:
                    authority_list.append(Version.AUTHORITY_DICT.get(key))
                except KeyError:
                    authority_list.append(0)
            if authority_list[0] == authority_list[1]:
                return
            result_flag = authority_list[0] < authority_list[1]

        def lt_elem_compare(elem_1: str, elem_2: str):
            nonlocal result_flag
            if elem_1.isdigit() and elem_2.isdigit():
                if elem_1 == elem_2:
                    return
                result_flag = elem_1 < elem_2
            elif elem_1.isdigit() and elem_2.isalpha():
                result_flag = False
            elif elem_1.isalpha() and elem_2.isdigit():
                result_flag = True
            elif elem_1 == "_" and elem_2 != "_":
                result_flag = True
            elif elem_1 != "_" and elem_2 == "_":
                result_flag = False
            elif elem_1.isalpha() and elem_2.isalpha():
                lt_authority_compare(elem_1, elem_2)

        for first, second in zip(lst_1, lst_2):
            lt_elem_compare(first, second)
        return result_flag


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"
