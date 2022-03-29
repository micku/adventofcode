local input = string.sub(debug.getinfo(1).short_src, 1, -10) .. "input"


function solve_part1 ()
    local f = io.open(input)

    local operations = {forward = 0, up = 0, down = 0}

    for line in f:lines() do
        for direction, unit in string.gmatch(line, "(%w+) (%w+)") do
            operations[direction] = operations[direction] + tonumber(unit)
        end
    end

    print(operations["forward"] * (operations["down"] - operations["up"]))
end


function solve_part2 ()
    local position = {horizontal = 0, depth = 0, aim = 0}

    function down (value)
        position["aim"] = position["aim"] + value
    end

    function up (value)
        position["aim"] = position["aim"] - value
    end

    function forward (value)
        position["horizontal"] = position["horizontal"] + value
        position["depth"] = position["depth"] + (position["aim"] * value)
    end

    local actions = {down = down, up = up, forward = forward}

    local f = io.open(input)

    for line in f:lines() do
        for direction, unit in string.gmatch(line, "(%w+) (%w+)") do
            actions[direction](tonumber(unit))
        end
    end

    print(position["horizontal"] * position["depth"])
end


solve_part1 ()
solve_part2 ()
