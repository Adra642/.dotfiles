local wezterm = require 'wezterm'

local config = wezterm.config_builder()

-- Color scheme:
 config.color_scheme = 'Kanagawa (Gogh)'
-- Spacedust
-- Nocturnal Winter
-- Galaxy
-- Chester
-- Sea Shells (Gogh)
-- Whimsy
-- lovelace

-- config = {
--   force_reverse_video_cursor = true,
-- 	colors = {
-- 		foreground = "#dcd7ba",
-- 		background = "#1f1f28",

-- 		cursor_bg = "#c8c093",
-- 		cursor_fg = "#c8c093",
-- 		cursor_border = "#c8c093",

-- 		selection_fg = "#c8c093",
-- 		selection_bg = "#2d4f67",

-- 		scrollbar_thumb = "#16161d",
-- 		split = "#16161d",

-- 		ansi = { "#090618", "#c34043", "#76946a", "#c0a36e", "#7e9cd8", "#957fb8", "#6a9589", "#c8c093" },
-- 		brights = { "#727169", "#e82424", "#98bb6c", "#e6c384", "#7fb4ca", "#938aa9", "#7aa89f", "#dcd7ba" },
-- 		indexed = { [16] = "#ffa066", [17] = "#ff5d62" },
--   }
-- }

-- Background
config.window_background_opacity = 0.9
config.enable_scroll_bar = true
config.window_close_confirmation = "NeverPrompt"

-- Font
config.font = wezterm.font('IosevkaTerm NF')
config.font_size = 16.0
config.line_height = 1.2

--Cursor
config.default_cursor_style = 'SteadyBar'
config.cursor_thickness = "1.0"

-- Tab bar:
config.hide_tab_bar_if_only_one_tab = true

return config
