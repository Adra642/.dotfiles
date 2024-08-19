local wezterm = require 'wezterm'


local module = {}


function module.set_color_scheme(config)
	config.colors = {
    	background = "#1f1f28",
		foreground = "#dcd7ba",

    	ansi = { 
			"#090618", 
			"#c34043", 
			"#76946a", 
			"#c0a36e", 
			"#7e9cd8", 
			"#957fb8", 
			"#6a9589", 
			"#DCD7BA" 
		},
    	brights = { 
			"#727169", 
			"#e82424", 
			"#98bb6c", 
			"#e6c384", 
			"#7fb4ca", 
			"#938aa9", 
			"#7aa89f", 
			"#C8C093" 
		},

		selection_bg = "#2d4f67",
		selection_fg = "#c8c093",

		cursor_border = "#969384",
	}
end

return module