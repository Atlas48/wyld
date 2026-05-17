local w, h = tonumber(arg[1]), tonumber(arg[2])
local new_w, new_h

if not w or not h then
	print("Requries a height and a width argument.")
	os.exit(1)
end

if w * 5 <= h * 7 then
    new_w, new_h = w, math.floor(w * 5 / 7 + 0.5)
else
    new_w, new_h = math.floor(h * 7 / 5 + 0.5), h
end

print(string.format("%dx%d", new_w, new_h))
