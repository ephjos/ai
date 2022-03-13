
import { Card } from "../Card";

export interface Player {
    id: number;
    name: string;
    score: number;
    hand: Card[];
    shown: Card[];
    // TODO: functions
}
