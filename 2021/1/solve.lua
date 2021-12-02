local input = string.sub(debug.getinfo(1).short_src, 1, -10) .. "input"

function solve_part1 ()
    local previous = nil
    local counter = 0

    for line in io.lines (input) do
        local current = tonumber(line)

        if previous then
            counter = counter + (current > previous and 1 or 0)
        end

        previous = current
    end

    print(counter)
end

Queue = {}
function Queue:new ()
    return {first = 0, last = -1}
end

function Queue.put (queue, value)
    local last = queue.last + 1
    queue.last = last
    queue[last] = value
end

function Queue.get (queue)
    local first = queue.first
    if first > queue.last then return nil end

    local value = queue[first]
    queue[first] = nil
    queue.first = first + 1
    return value
end

function Queue.sum (queue)
    local sum = 0

    for key, value in pairs(queue) do
        sum = sum + value
    end

    return sum - queue.first - queue.last
end

function solve_part2 ()
    local q = Queue:new ()

    local f = io.open(input)
    for i=1,3 do
        Queue.put(q, tonumber(f:read()))
    end

    local previous = Queue.sum(q)
    local counter = 0

    for l in f:lines() do
        Queue.get(q)
        Queue.put(q, tonumber(l))

        local current = Queue.sum(q)

        counter = counter + (current > previous and 1 or 0)

        previous = current
    end

    f:close()

    print(counter)
end

solve_part1()
solve_part2()
