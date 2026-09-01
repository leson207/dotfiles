-- build list from same directory
swayimg.imagelist.enable_adjacent(true)
swayimg.imagelist.enable_recursive(false)

-- sort by modification time
swayimg.imagelist.set_order("mtime")
swayimg.imagelist.enable_reverse(true)

-- clean UI
swayimg.viewer.set_text("topleft", {})
swayimg.viewer.set_text("topright", {})
swayimg.viewer.set_text("bottomleft", {})

swayimg.text.set_timeout(0)
swayimg.text.set_status_timeout(0)

-- quit
swayimg.viewer.on_key("q", function()
    swayimg.exit()
end)

-- IMPORTANT: use viewer switching (this is correct in 5.5)
swayimg.viewer.on_key("Left", function()
    swayimg.viewer.switch_image("prev")
end)

swayimg.viewer.on_key("Right", function()
    swayimg.viewer.switch_image("next")
end)
