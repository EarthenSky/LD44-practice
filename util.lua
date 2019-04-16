local Util = {}

-- This function converts floating point numbers into integers.
function Util.toint(floatingPointNumber)
    return math.floor(floatingPointNumber)
end

function Util.round(num)
    return math.floor(num+0.5)
end


return Util
