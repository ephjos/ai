
import { Card } from "./Card";
import { Player } from "./Player/Player";

export type Game = {
    players: Player[];
    stock: Card[];
    discard: Card[];
};

export function getWinner(game: Game): Player | null {
    // TODO: implement
    // over 500
    // if multiple over, player who went out wins (current turn)
    return null;
}

// Plays game, returning winner
export function playGame(game: Game): Player {
    let turn: number = 0;
    let winner: Player | null = null;

    while (!winner) {
        while (true) {
            const player = game.players[turn];
            // TODO: draw
            // TODO: optional amount of moves
            // TODO: discard
            if (player.hand.length === 0) {
                break;
            }
        }
        // TODO: end round
        // TODO: calculate points for round
        // TODO: set player points
        winner = getWinner(game);
        // TODO: increment turn
    }



    return winner;
}

