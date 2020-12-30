#!/usr/bin/env python
from agent import Agent, QLearning, RandomChoice
from common import Result
from game import TicTacToeGame
import matplotlib.pyplot as plt

class Battle:
    def __init__(
            self,
            player_1: Agent,
            player_2: Agent,
    ):
        self.player_1 = player_1
        self.player_2 = player_2

    def run(self, n=100):
        tie, x, o = 0, 0, 0
        ties, xs, os = [], [], []
        game = TicTacToeGame(self.player_1, self.player_2)
        for i in range(1,n+1):
            res = game.play()
            if res == Result.Tie:
                tie += 1
            elif res == Result.X_Win:
                x += 1
            elif res == Result.O_Win:
                o += 1
            ties.append(tie/i)
            xs.append(x/i)
            os.append(o/i)
            temp = self.player_1
            self.player_1 = self.player_2
            self.player_2 = temp
        return n, ties, xs, os

    def plot_run(self, total, ties, xs, os, fn=None):
        plt.plot(ties, label='Tie')
        plt.plot(xs, label=self.player_1.name + ' (X)')
        plt.plot(os, label=self.player_2.name + ' (O)')

        plt.xlabel('Iteration')
        plt.ylabel('Probability of Result')
        plt.legend()

        if fn:
            plt.savefig(fn)
            print(f'Saved figure to {fn}')
        else:
            plt.show()

        plt.close()

    def run_and_plot(self, n=100, fn=None):
        self.plot_run(*self.run(n), fn)

if __name__ == "__main__":
    agent_1, agent_2 = RandomChoice(), QLearning()
    n = 500000
    battle = Battle(agent_1, agent_2)
    battle.run_and_plot(n)
    battle = Battle(agent_2, agent_1)
    battle.run_and_plot(n)

