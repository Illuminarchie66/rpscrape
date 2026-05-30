import os
import tomli

from pathlib import Path
from collections.abc import Mapping
from typing import Any


class Settings:
    def __init__(self) -> None:
        self.toml: Mapping[str, Any] | None = self.load_toml()

        if self.toml is None:
            self.fields: list[str] = []
            self.csv_header: str = ''
            return

        self.fields = self.get_fields()
        self.csv_header = ','.join(self.fields)

    def get_fields(self) -> list[str]:
        fields: list[str] = []

        if self.toml is None:
            return fields

        for group in self.toml.get('fields', {}):
            if group == 'betfair' and not self.toml.get('betfair_data', False):
                continue
            for field, enabled in self.toml['fields'][group].items():
                if enabled:
                    fields.append(field)

        return fields

def load_toml(self) -> Mapping[str, Any] | None:
    ROOT_DIR = Path(__file__).resolve().parents[1]

    default_path = ROOT_DIR / 'settings' / 'default_settings.toml'
    user_path = ROOT_DIR / 'settings' / 'user_settings.toml'

    path = user_path if user_path.is_file() else default_path

    if path == default_path and not default_path.is_file():
        raise FileNotFoundError(f'{default_path} does not exist')

    try:
        with path.open('rb') as f:
            return tomli.load(f)
    except tomli.TOMLDecodeError:
        print(f'TomlParseError: {path}')
        return None
