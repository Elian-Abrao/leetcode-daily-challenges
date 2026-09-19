class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        ans = []
        path = []

        def dfs(index: int) -> None:
            # All characters processed, save the current permutation.
            if index == len(s):
                ans.append("".join(path))
                return

            ch = s[index]

            # Digits have only one form, so continue without branching.
            if not ch.isalpha():
                path.append(ch)
                dfs(index + 1)
                path.pop()
                return

            # Letters branch into lowercase and uppercase choices.
            path.append(ch.lower())
            dfs(index + 1)
            path.pop()

            path.append(ch.upper())
            dfs(index + 1)
            path.pop()

        dfs(0)
        return ans