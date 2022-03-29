local input = string.sub(debug.getinfo(1).short_src, 1, -10) .. "input"


function solve_part1 ()
    local f = io.open (input)

    local diagnostic_values = {}
    local count = 0

    for diagnostic in f:lines() do
        for i = 1, #diagnostic do
            diagnostic_values[i] = (diagnostic_values[i] or 0) + diagnostic:sub(i, i)
        end
        count = count + 1
    end

    local gamma_rate = ""
    local epsilon_rate = ""
    local half_count = count / 2

    for k,v in ipairs(diagnostic_values) do
        gamma_rate = gamma_rate .. ((v > half_count) and "1" or "0")
        epsilon_rate = epsilon_rate .. ((v > half_count) and "0" or "1")
    end

    print(tonumber(gamma_rate, 2) * tonumber(epsilon_rate, 2))
end


function solve_part2 ()
    local f = io.open (input)

    local diagnostic_values = {}
    local count = 0

    for diagnostic in f:lines() do
        count = count + 1
        diagnostic_values[count] = {}
        for i = 1, #diagnostic do
            diagnostic_values[count][i] = diagnostic:sub(i, i)
        end
    end


    function filter (t, index, fn)
        local positives = 0

        for k, v in ipairs(t) do
            positives = positives + v[index]
        end

        -- 
    end

    for k,v in ipairs(diagnostic_values) do
        for k1,v1 in ipairs(v) do
            print(k .. " " .. v1)
        end
    end
    print(count)
end


solve_part1()
solve_part2()
