class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}
        players = set()

        for winner, loser in matches:
            loss_count[loser] = loss_count.get(loser, 0) + 1
            players.add(winner)
            players.add(loser)

        finalWin = [player for player in players if loss_count.get(player, 0) == 0]
        finalLoss = [player for player in players if loss_count.get(player, 0) == 1]

        return [sorted(finalWin), sorted(finalLoss)]