# TODO: use gettext
import collections
import json
import pathlib

# TODO: Use package resources
# Path to language files
LANGUAGE_FILES = {
    "English": "en.json",
    "Japanese": "jp.json",
}


class LanguageTexts(collections.defaultdict):
    @staticmethod
    def available_languages():
        return frozenset(LANGUAGE_FILES.keys())

    def __init__(self, language="English"):
        try:
            language_file = pathlib.Path(__file__).parent / LANGUAGE_FILES[language]
            translations = json.loads(language_file.read_text())
        except KeyError:
            print(f"Language '{language}' not found.")
        except FileNotFoundError:
            print(f"Language file ({language_file}) for {language} not found.")
        super().__init__(lambda: "Missing localization string", translations)
