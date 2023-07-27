from typing import List


class UI:
    def __init__(self, generator):
        self.generator = generator

    def show_welcome(self):
        print("=====Welcome to MadLibz=====")
        print("=====Complete the sentences using=====\n")
        for idx, title in enumerate(self.generator.titles):
            print(f"{idx}.\t{title}")

    def prompt_completion(self, index: int) -> List[str]:
        question = self.generator.items[index]
        answers: List[str] = []
        print("Please provide the following:")
        for blank in question.blanks:
            ans = input(f"\t{blank} => ")
            answers.append(ans)
        return answers

    def run(self):
        self.show_welcome()
        index = int(input("Choose one of the indices:\t"))
        answers = self.prompt_completion(index)
        print(self.generator.get_final_story(index, answers))
