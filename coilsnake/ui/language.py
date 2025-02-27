from datetime import datetime
import logging
import os
import json
from shutil import copyfile
import time
import sys
from ccscript import ccc
from collections import defaultdict

# Path to language files
LANGUAGE_FILES = {
    "English": "coilsnake/lang/en.json",
    "Japanese": "coilsnake/lang/jp.json",
}


class TranslationStringManager:
    _TRANSLATIONS_LANGUAGE_NOT_LOADED = defaultdict( lambda: "Translation not loaded" )

    @staticmethod
    def _json_to_translations(json_data):
        missing = "Missing localization string"
        return defaultdict(lambda: missing, json_data)

    @classmethod
    def _load_language(cls, language):
        file_path = LANGUAGE_FILES.get(language, None)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                json_data = json.load(file)
            return cls._json_to_translations(json_data)
        except:
            return None

    def __init__(self):
        self.translations = self._TRANSLATIONS_LANGUAGE_NOT_LOADED

    def get(self, string_name: str) -> str:
        return self.translations[string_name]

    def change_language(self, language: str) -> None:
        translations = self._load_language(language)
        if not translations:
            log.error("Unable to load translation file for language '%s'", language)
            return
        self.translations = translations
        self._update_translated_strings()

    def _update_translated_strings(self) -> None:
        pass

strings = TranslationStringManager()
strings.change_language("Japanese")