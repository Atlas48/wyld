interface CardStackExport {
  name: string;
  type: "deck" | "hand" | "pile";
  description: string;
  img: string;
  system: Record<string, unknown>;
  cards: CardExport[];
  width: number | null;
  height: number | null;
  rotation: number;
  displayCount: boolean;
  ownership: Record<string, number>;
  flags: Record<string, Record<string, unknown>>;
  _stats?: Record<string, unknown>;
  folder: string | null;
  sort: number;
  _id?: string;
}

interface CardExport {
  name: string;
  type: string;
  _id?: string;
  description: string;
  system: Record<string, unknown>;
  suit: string;
  value: number | null;
  back: CardFace;
  faces: CardFace[];
  face: number | null;
  drawn: boolean;
  origin: string | null;
  width: number | null;
  height: number | null;
  rotation: number;
  sort: number;
  flags: Record<string, Record<string, unknown>>;
}

interface CardFace {
  name: string;
  img: string;
  text: string;
}

