local wezterm = require 'wezterm'
local module = {}
function module.set_color_scheme(config)

    config.colors = {
        background = "#1F1F28",
        foreground = "#DCD7BA",

        ansi = { 
            "#090618", 
            "#C34043", 
            "#76946A", 
            "#C0A36E", 
            "#7E9CD8", 
            "#957FB8", 
            "#6A9589", 
            "#DCD7BA" 
        },
        brights = { 
            "#727169", 
            "#E82424", 
            "#98BB6C", 
            "#E6C384", 
            "#7FB4CA", 
            "#938AA9", 
            "#7AA89F", 
            "#C8C093" 
        },

        selection_bg = "#2D4F67",
        selection_fg = "#C8C093",

        cursor_border = "#969384",
    }    
    
end
return module