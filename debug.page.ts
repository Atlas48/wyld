export const url = "./debug.json";

export default function(data: Lume.Data) {
  return JSON.stringify([data.search.data(),data.search.files()], null, 2);
}
