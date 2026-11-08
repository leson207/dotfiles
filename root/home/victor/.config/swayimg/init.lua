-- build list from same directory
swayimg.imagelist.adjacent = true
swayimg.imagelist.recursive = false

-- sort by modification time
swayimg.imagelist.order = "mtime"
swayimg.imagelist.reverse = true

-- clean UI
swayimg.viewer.text = {
    topleft = {},
    topright = {},
    bottomleft = {},
}

swayimg.text.timeout = 0
swayimg.text.status_timeout = 0

-- quit
swayimg.viewer.on_key("q", function()
    swayimg.exit()
end)

-- navigation
swayimg.viewer.on_key("Left", function()
    swayimg.viewer.switch_image("prev")
end)

swayimg.viewer.on_key("Right", function()
    swayimg.viewer.switch_image("next")
end)
