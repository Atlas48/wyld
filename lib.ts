import deflist from "npm:markdown-it-deflist";

export const conf = {
	prettyUrls: false
};

export const mdconf = {
	plugins: [deflist]
}

export const slugconf = {
	lower: true,
	remove: /[!()!"£$%^\*\\]/g
}

export function partial<T extends (...args: any[]) => any>( fn: T, ...boundArgs: any[]): (...args: any[]) => ReturnType<T> {
  return (...args: any[]) => fn(...boundArgs, ...args.slice(0, fn.length - boundArgs.length));
}
