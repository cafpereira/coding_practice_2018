class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        # Corner-cases
        if not all(word in dictV for word in {start, end}):
            return 0

        queue = []
        dist = {}
        visited = set()
        dic = set(dictV)

        queue.append(start)
        visited.add(start)
        dist[start] = 1

        # Run BFS search
        while queue:
            cur = queue.pop(0)
            if cur == end:
                return dist[cur]

            candidates = dic - visited
            for cand in candidates:
                if self.edit_distance(cur, cand) == 1:
                    visited.add(cand)
                    queue.append(cand)
                    dist[cand] = dist[cur] + 1

        # No transformation path found
        return 0

    def edit_distance(self, word1, word2):
        diff = 0
        n = len(word1)  # Assume words have same length
        for i in range(n):
            if word1[i] != word2[i]:
                diff = diff + 1
        return diff

