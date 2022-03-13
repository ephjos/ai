
enum Suit {
    Clubs,
    Diamonds,
    Hearts,
    Spades,
}

enum Value {
    One,
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Jack,
    Queen,
    King,
    Ace
}

export type Card = {
  value: Value,
  suit: Suit,
}

export function createDeck(): Card[] {
    return [
        // Clubs
        { value: Value.One, suit: Suit.Clubs },
        { value: Value.Two, suit: Suit.Clubs },
        { value: Value.Three, suit: Suit.Clubs },
        { value: Value.Four, suit: Suit.Clubs },
        { value: Value.Five, suit: Suit.Clubs },
        { value: Value.Six, suit: Suit.Clubs },
        { value: Value.Seven, suit: Suit.Clubs },
        { value: Value.Eight, suit: Suit.Clubs },
        { value: Value.Nine, suit: Suit.Clubs },
        { value: Value.Ten, suit: Suit.Clubs },
        { value: Value.Jack, suit: Suit.Clubs },
        { value: Value.Queen, suit: Suit.Clubs },
        { value: Value.King, suit: Suit.Clubs },
        { value: Value.Ace, suit: Suit.Clubs },
        // Diamonds
        { value: Value.One, suit: Suit.Diamonds },
        { value: Value.Two, suit: Suit.Diamonds },
        { value: Value.Three, suit: Suit.Diamonds },
        { value: Value.Four, suit: Suit.Diamonds },
        { value: Value.Five, suit: Suit.Diamonds },
        { value: Value.Six, suit: Suit.Diamonds },
        { value: Value.Seven, suit: Suit.Diamonds },
        { value: Value.Eight, suit: Suit.Diamonds },
        { value: Value.Nine, suit: Suit.Diamonds },
        { value: Value.Ten, suit: Suit.Diamonds },
        { value: Value.Jack, suit: Suit.Diamonds },
        { value: Value.Queen, suit: Suit.Diamonds },
        { value: Value.King, suit: Suit.Diamonds },
        { value: Value.Ace, suit: Suit.Diamonds },
        // Hearts
        { value: Value.One, suit: Suit.Hearts },
        { value: Value.Two, suit: Suit.Hearts },
        { value: Value.Three, suit: Suit.Hearts },
        { value: Value.Four, suit: Suit.Hearts },
        { value: Value.Five, suit: Suit.Hearts },
        { value: Value.Six, suit: Suit.Hearts },
        { value: Value.Seven, suit: Suit.Hearts },
        { value: Value.Eight, suit: Suit.Hearts },
        { value: Value.Nine, suit: Suit.Hearts },
        { value: Value.Ten, suit: Suit.Hearts },
        { value: Value.Jack, suit: Suit.Hearts },
        { value: Value.Queen, suit: Suit.Hearts },
        { value: Value.King, suit: Suit.Hearts },
        { value: Value.Ace, suit: Suit.Hearts },
        // Spades
        { value: Value.One, suit: Suit.Spades },
        { value: Value.Two, suit: Suit.Spades },
        { value: Value.Three, suit: Suit.Spades },
        { value: Value.Four, suit: Suit.Spades },
        { value: Value.Five, suit: Suit.Spades },
        { value: Value.Six, suit: Suit.Spades },
        { value: Value.Seven, suit: Suit.Spades },
        { value: Value.Eight, suit: Suit.Spades },
        { value: Value.Nine, suit: Suit.Spades },
        { value: Value.Ten, suit: Suit.Spades },
        { value: Value.Jack, suit: Suit.Spades },
        { value: Value.Queen, suit: Suit.Spades },
        { value: Value.King, suit: Suit.Spades },
        { value: Value.Ace, suit: Suit.Spades },
    ];
}

// Fisher–Yates shuffle
//   See: https://bost.ocks.org/mike/shuffle/
export function shuffleInPlace<T>(array: T[]): T[] {
    let m = array.length;
    let t: T;
    let i: number;

  // While there remain elements to shuffle…
  while (m) {

    // Pick a remaining element…
    i = Math.floor(Math.random() * m--);

    // And swap it with the current element.
    t = array[m];
    array[m] = array[i];
    array[i] = t;
  }

  return array;
}

