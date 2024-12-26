# TODO: use gettext
import collections
import json
import os
import pathlib
import sys
import tkinter.ttk

# fix up tcl/tk if not set up (otherwise, assume it's correct!)
lib_base_prefix = pathlib.Path(sys.base_prefix) / "lib"
os.environ.setdefault("TCL_LIBRARY", str(lib_base_prefix / "tcl8.6"))
os.environ.setdefault("TK_LIBRARY", str(lib_base_prefix / "tk8.6"))

# TODO: Use package resources
# Path to language files
LANGUAGE_FILES = {
    "English": "en.json",
    "Japanese": "jp.json",
}


class LanguageTexts(collections.UserDict):
    @staticmethod
    def available_languages():
        return frozenset(LANGUAGE_FILES.keys())

    def __init__(self, language="English", missing="Missing localization string"):
        self.missing = missing
        try:
            language_file = pathlib.Path(__file__).parent / LANGUAGE_FILES[language]
            translations = json.loads(language_file.read_text())
        except KeyError:
            print(f"Language '{language}' not found.")
        except FileNotFoundError:
            print(f"Language file ({language_file}) for {language} not found.")
        super().__init__(translations)

    def __getitem__(self, key) -> str:
        return self.data.get(key, self.missing)


class TkLanguageTexts(LanguageTexts):
    def __init__(
        self, parent, language="English", missing="Missing localization string"
    ):
        self.parent = parent
        super().__init__(language, missing)

    def __getitem__(self, key) -> tkinter.ttk.Label:
        return tkinter.ttk.Label(self.parent, text=self.data.get(key, self.missing))


__all__ = ["LanguageTexts", "TkLanguageTexts"]
