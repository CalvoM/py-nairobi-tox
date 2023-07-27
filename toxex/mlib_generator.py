import functools
import itertools
import json
from typing import Any, Dict, List


class MadLibsGenerator:
    def __init__(self, source_file: str = "./data.json"):
        with open(source_file) as f:
            self._content = json.loads(f.read()).get("templates", [])

    @functools.cached_property
    def titles(self) -> List[str]:
        """Get list of titles"""
        return [t["title"] for t in self.content]

    def details(self):
        for c in self.content:
            print(c["title"], len(c["blanks"]), len(c["value"]))

    @property
    def content(self) -> List[Dict[str, Any]]:
        return self._content

    def get_final_story(self, index: int, answers: List[str]):
        question = self.content[index]
        final_comp = list(itertools.zip_longest(question.get("value"), answers))[:-1]
        story = ""
        for words in final_comp:
            if words[1]:
                story += words[0] + words[1]
            else:
                story += words[0]
        return story
