--Double commented code (----) is not a note, but removed code.

-- Constant variables.
ScreenSize = {x=640, y=640}
isMenu = true

function love.load()
    -- Set up the window.
    love.window.setMode(ScreenSize.x, ScreenSize.y, {resizable=false, vsync=true})
    love.window.setTitle("Love2D Template")
    love.graphics.setBackgroundColor(0, 0, 0, 255)

    -- Load assets here.
    menuImg = love.graphics.newImage("resc/tile.png")

    -- Modules and classes are loaded here.
    menu = require("src/menu")

    -- Any initialization code goes here.

end

-- Only drawing and maybe come conditional statements go here.
function love.draw()
    if isMenu then
        menu.draw()
    else
        --sequencer.draw()  -- let the sequencer choose what to draw.
    end

    -- Print the current scene in the top left corner and set colour + font size
    love.graphics.setFont(love.graphics.newFont(18))
    love.graphics.setColor(250, 250, 250, 255)
    love.graphics.print(tostring(isMenu), 2, 2)
end

-- No drawing code, Math or physics code here.
function love.update(dt)
    if isMenu then
        menu.update()
    else
        -- let the sequencer choose what part of the game to update
        --sequencer.update()
    end
end
