-- this is a class
-- this has the lookup tables
Map = {}

function Map:new()
    -- Add member variables here.
    selfObj = {}
    selfObj.hello = 0

    -- Make this into a class.
    self.__index = self
    return setmetatable(selfObj, self)
end

function Map:load()

end

return Map
