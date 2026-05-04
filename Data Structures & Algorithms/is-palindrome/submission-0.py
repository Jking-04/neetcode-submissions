class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.lower()
        left_ptr=0
        right_ptr=len(s)-1

        while left_ptr<right_ptr:
            if not s[left_ptr].isalnum():
                left_ptr+=1
            elif not s[right_ptr].isalnum():
                right_ptr-=1
            else:
                if s[left_ptr] != s[right_ptr]:
                    print(s[left_ptr])
                    print(s[right_ptr])
                    return False
                left_ptr+=1
                right_ptr-=1
      
        return True
        