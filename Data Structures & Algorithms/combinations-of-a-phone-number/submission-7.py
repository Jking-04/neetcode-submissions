class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digit_to_char = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        self.result = []
        self.backtrack(digits,path="")
        return self.result

    def backtrack(self, digits, path):
        if not digits:
            if path:
                self.result.append(path)
            return

        new_num = digits[0]
        for letter in self.digit_to_char[new_num]:
            new_path = path + letter
            self.backtrack(digits[1:],path=new_path)

        