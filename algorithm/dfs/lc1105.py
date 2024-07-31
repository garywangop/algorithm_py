from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        self.res = float("inf")
        def dfs(total_height, book_idx):
            if book_idx == len(books):
                self.res = min(self.res, total_height)
                return
            cur_width = books[book_idx][0]
            cur_height = books[book_idx][1]

            book_idx += 1
            # to next level
            dfs(total_height + cur_height, book_idx)
            # add more books to current level

            while book_idx < len(books) and cur_width + books[book_idx][0] <= shelfWidth:
                cur_width += books[book_idx][0]
                cur_height = max(cur_height, books[book_idx][1])
                book_idx += 1
                dfs(total_height + cur_height, book_idx)
        dfs(0, 0)
        return self.res


if __name__ == '__main__':
    sol = Solution()
    books1, shelfWidth1 = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4
    print(6 == sol.minHeightShelves(books1, shelfWidth1))

    books2, shelfWidth2 = [[1,3],[2,4],[3,2]], 6
    print(4 == sol.minHeightShelves(books2, shelfWidth2))