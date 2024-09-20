local wezterm = require 'wezterm'
local mux = wezterm.mux
local color = require 'color'

local config = wezterm.config_builder()

-- Color scheme:

-- Spacedust
-- Nocturnal Winter
-- Galaxy
-- Chester
-- Sea Shells (Gogh)
-- Whimsy
-- lovelace

color.set_color_scheme(config)

-- Background
config.window_background_opacity = 0.85
config.window_close_confirmation = "NeverPrompt"
config.enable_scroll_bar = false

wezterm.on('gui-attached', function(domain)
  -- maximize all displayed windows on startup
  local workspace = mux.get_active_workspace()
  for _, window in ipairs(mux.all_windows()) do
    if window:get_workspace() == workspace then
      window:gui_window():maximize()
    end
  end
end)

config.alternate_buffer_wheel_scroll_speed = 5

config.window_padding = {
    left = 20,
    right = 20,
    top = 15,
    bottom = 5,
  }

-- Font
config.font = wezterm.font{
    family='IosevkaTerm NF',
    weight= 'DemiBold',
}

config.bold_brightens_ansi_colors = false;

config.window_frame = {
  font = wezterm.font('IosevkaTerm NF', { weight = 'Bold' }),
  font_size = 12,
}

config.font_size = 15
config.line_height = 1.24

--Cursor
config.default_cursor_style = 'SteadyUnderline'
config.cursor_thickness = "1.0"

-- Tab bar:
config.enable_tab_bar = false

return config
