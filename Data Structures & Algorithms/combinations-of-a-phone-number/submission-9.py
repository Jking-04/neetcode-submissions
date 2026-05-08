class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
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
        self.backtrack(i=0,path="")
        return self.result

    def backtrack(self, i, path):
        if i == len(self.digits):
            if path:
                self.result.append(path)
            return

        new_num = self.digits[i]
        for letter in self.digit_to_char[new_num]:
            self.backtrack(i+1,path=path+letter)

        