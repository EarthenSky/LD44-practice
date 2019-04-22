-- this module loads info from the disk and gives it to the map clas.

MapLoader = {}

--This is a lookup table for finding maps by their name.  --TODO: I dont think i need this anymore, i can just have them all iun the same directory and then that works just fine...
local mapLookup = {
    ["test-map"] = "maps/test.mp"
}

-- TODO: have a lookup table here for map name to disk position.
function MapLoader.fromdisk()

end

return MapLoader
