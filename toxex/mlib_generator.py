import functools
import itertools
import json
from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class MadLibItem:
    title: str
    blanks: List[str]
    value: List[str]


class MadLibsGenerator:
    def __init__(self, source_file: str = "./data.json"):
        with open(source_file) as f:
            content = json.loads(f.read()).get("templates", [])
            self._madLibItems: List[MadLibItem] = list()
            for mt in content:
                madlibItem = MadLibItem(mt["title"], mt["blanks"], mt["value"])
                self._madLibItems.append(madlibItem)

    @functools.cached_property
    def titles(self) -> List[str]:
        """Get list of titles"""
        return [t.title for t in self._madLibItems]

    def details(self):
        for mt in self._madLibItems:
            print(mt.title, len(mt.blanks), len(mt.value))

    @property
    def items(self) -> List[MadLibItem]:
        return self._madLibItems

    def get_final_story(self, index: int, answers: List[str]):
        question = self.items[index]
        final_comp = list(itertools.zip_longest(question.value, answers))[:-1]
        story = ""
        for words in final_comp:
            if words[1]:
                story += words[0] + words[1]
            else:
                story += words[0]
        return story
