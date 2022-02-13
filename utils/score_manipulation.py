import random


class ScoreManipulation:

    @staticmethod
    def score_generator():
        score = random.randint(1, 999)
        return score

    @staticmethod
    def approval(score: int) -> str:
        if score <= 299:
            return "Reprovado"
        return "Aprovado"

    @staticmethod
    def limit_calculator(score: int, income: float) -> float:
        card_limit = 0

        if 300 <= score <= 599:
            card_limit = 1000.00
        elif 600 <= score <= 799:
            if income > 2000:
                card_limit = income / 2
            else:
                card_limit = 1000.00
        elif 800 <= score <= 959:
            card_limit = income * 2

        elif score >= 960:
            card_limit = 1000000.000

        return card_limit




