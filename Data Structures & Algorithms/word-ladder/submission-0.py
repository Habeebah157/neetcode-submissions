class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st = set(wordList)
        res = 0
        m = len(beginWord)
        words = deque()
        words.append(beginWord)
        while words:
            res += 1
            length = len(words)
            print(length)
            for _ in range(length):
                word = words.popleft()
                for j in range(m):
                    ch = word[j]
                    for c in range(ord('a'), ord('z') + 1):
                        word = word[:j] + chr(c) + word[j+1:]
                        if word not in st:
                            continue
                        if word == endWord:
                            return res + 1
                        st.remove(word)
                        words.append(word)
                    word = word[:j] + ch + word[j+1:]
        
        return 0
            