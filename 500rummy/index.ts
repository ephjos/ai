
import { Card, createDeck, shuffleInPlace } from "./src/Card";

const deck = createDeck();
console.log(JSON.stringify(deck, null, 2))
shuffleInPlace(deck)
console.log(JSON.stringify(deck, null, 2))

