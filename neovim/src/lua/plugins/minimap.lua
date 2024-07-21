return {
	"gorbit99/codewindow.nvim",
	config = function()
		local codewindow = require("codewindow")
		codewindow.setup({
			width_multiplier = 4,
			minimap_width = 10,
			auto_enable = true,
		})
		codewindow.apply_default_keybinds()
	end,
}
