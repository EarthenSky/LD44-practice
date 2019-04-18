-- this module loads info from the disk and gives it to the map clas.

MapLoader = {}

--This is a lookup table for finding maps by their name.
local mapLookup = {
    ["test-map"] = "maps/test.mp"
}

-- TODO: have a lookup table here for map name to disk position.
function MapLoader.fromdisk()

end

return MapLoader
