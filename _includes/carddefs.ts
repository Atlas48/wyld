**
 * Represents a Card Stack (Deck, Hand, or Pile) for import/export.
 */
interface CardStackExport {
  /** Core document type identifier; should be "Cards". */
  type: "Cards";
  /** Unique document ID (optional on import; can be generated). */
  _id?: string;
  /** Name of the card stack. */
  name: string;
  /** Type of stack: "deck", "hand", or "pile". */
  stackType: "deck" | "hand" | "pile";
  /** Description of the stack. */
  description?: string;
  /** Default card back image path. */
  img?: string;
  /** Array of embedded Card documents. */
  cards: CardExport[];
  /** Permission object (default/owner/user access). */
  permission?: Record<string, string>;
  /** Folder ID if the stack is organized in a folder. */
  folder?: string;
  /** Sort index for ordering within a folder. */
  sort?: number;
  /** System-specific data extensions. */
  system?: Record<string, unknown>;
  /** Flags for module/custom data. */
  flags?: Record<string, Record<string, unknown>>;
}

/**
 * Represents a single Card within a CardStack.
 */
interface CardExport {
  /** Core document type identifier; should be "Card". */
  type: "Card";
  /** Unique card ID (optional on import). */
  _id?: string;
  /** Name of the card. */
  name: string;
  /** Card type (e.g., "base" or custom types). */
  cardType: string;
  /** Suit of the card (e.g., "Hearts"). */
  suit: string;
  /** Numerical value of the card. */
  value: number;
  /** Whether the card has been drawn from its original deck. */
  drawn?: boolean;
  /** Origin deck ID (used for reset operations). */
  origin?: string;
  /** Card dimensions and rotation. */
  width?: number;
  height?: number;
  rotation?: number;
  /** Text description of the card. */
  description?: string;
  /** Array of face definitions (at least one). */
  faces: CardSide[];
  /** Single back definition. */
  back: CardSide;
  /** System-specific data extensions. */
  system?: Record<string, unknown>;
  /** Flags for module/custom data. */
  flags?: Record<string, Record<string, unknown>>;
}

/**
 * Defines one face of a card.
 */
interface CardSide {
  /** Name identifier for the face. */
  name: string;
  /** Image path for the face. */
  img?: string;
  /** Text description of the face. */
  text?: string;
}

