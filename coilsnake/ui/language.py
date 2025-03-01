from collections import defaultdict
import json
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Language:
    iso639_1_name: str
    full_name: str
    alternative_names: List[str]

    def get_json_path(self) -> str:
        return f"coilsnake/lang/{self.iso639_1_name}.json"

LANGUAGES: List[Language] = [
    Language("en", "English", []),
    Language("ja", "日本語", ["Japanese", "jp"]),
]

def _build_language_lookup() -> Dict[str, Language]:
    ret = {}
    for language in LANGUAGES:
        for option in (language.iso639_1_name, language.full_name, *language.alternative_names):
            lookup = option.lower()
            assert lookup not in ret, "duplicate language name"
            ret[lookup] = language
    return ret

_LANGUAGE_LOOKUP = _build_language_lookup()

def get_language_by_string(language_str: str) -> Optional[Language]:
    return _LANGUAGE_LOOKUP.get(language_str.lower(), None)

class TranslationStringManager:
    _TRANSLATIONS_LANGUAGE_NOT_LOADED = defaultdict( lambda: "Translation not loaded" )

    @staticmethod
    def _json_to_translations(json_data):
        missing = "Missing localization string"
        return defaultdict(lambda: missing, json_data)

    @classmethod
    def _load_language(cls, language: Language):
        try:
            with open(language.get_json_path(), "r", encoding="utf-8") as file:
                json_data = json.load(file)
            return cls._json_to_translations(json_data)
        except:
            return None

    def __init__(self):
        self.translations = self._TRANSLATIONS_LANGUAGE_NOT_LOADED
        self.callbacks = set()

    def get(self, string_name: str) -> str:
        return self.translations[string_name]

    def change_language(self, language: Language = None, language_name: str = None) -> None:
        if not language:
            language = get_language_by_string(language_name)
        if not language:
            return False
        translations = self._load_language(language)
        if not translations:
            return False
        self.translations = translations
        for cb in self.callbacks:
            cb()
        return True

    def register_callback(self, cb, invoke=True):
        self.callbacks.add(cb)
        if invoke:
            cb()

global_strings = TranslationStringManager()
