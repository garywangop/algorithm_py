from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        idx, m = 0, []

        while idx < len(hand):
            cur, cnt = hand[idx], 0
            while idx < len(hand) and cur == hand[idx]:
                idx += 1
                cnt += 1
            m.append([cur, cnt])

        for i in range(len(m)):
            if m[i][1] == 0:
                continue

            cur_min_val, cur_min_cnt = m[i][0], m[i][1]
            m[i][1] = 0
            for j in range(1, groupSize):
                if i + j >= len(m) or m[i + j][0] != cur_min_val + j or m[i + j][1] < cur_min_cnt:
                    return False
                m[i + j][1] -= cur_min_cnt

        return True



if __name__ == '__main__':
    sol = Solution()
    hand1, groupSize1 = [1,2,3,6,2,3,4,7,8], 3
    print(True == sol.isNStraightHand(hand1, groupSize1))
    hand2, groupSize2 = [1,2,3,4,5], 4
    print(False == sol.isNStraightHand(hand2, groupSize2))
    hand3, groupSize3 = [1, 1, 2, 2, 3, 3], 2
    print(False == sol.isNStraightHand(hand3, groupSize3))