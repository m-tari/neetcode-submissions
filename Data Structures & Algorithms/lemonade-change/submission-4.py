class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 10:
                if fives == 0:
                    return False
                else:
                    fives -= 1
                    tens += 1

            elif bill == 20:
                if (
                    (fives < 3 and tens == 0) or
                    (fives == 0)
                ):
                    return False
                elif tens:
                    fives -= 1
                    tens -= 1
                else:
                    fives -= 3

            else:
                fives += 1

        return True
