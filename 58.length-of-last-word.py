class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        last_position = length - 1

        for i in range(length-1, -1, -1):
            if s[i] != ' ':
                last_position = i
                break

        first_position = 0
        for i in range(last_position-1, -1, -1):
            if s[i] == ' ':
                first_position = i + 1
                break

        print(s[first_position:last_position])

        return last_position - first_position + 1
"""

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

1. Find the last word
Approach 1: Go through each word until the end of the sentence, which is the last word
Approach 2: Search from the end of the string
- if there's no space left => terminate of the last word
- find for the second space character, or can't find any character at all => start of the last word 
=> Choose the second approach
2. Count the length of the last word
"""


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"))
    print(solution.lengthOfLastWord("   fly me   to   the moon  "))
    print(solution.lengthOfLastWord("luffy is still joyboy"))