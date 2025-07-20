 Neovim with PlatformIO
![hmm](https://github.com/ironlungx/icons/blob/main/screenshot.png?raw=true)

## Quick start
1. Install `clangd`
2. Setup LSP server for neovim `require('lspconfig').clangd.setup({})`
3. Clone this repository `$ git clone https://github.com/ironlungx/nvim-pio`
4. Set `board` and `platform`
5. `pio init --ide vim`
6. `python3 conv.py`
7. Open Neovim. LSP should now work! If not, open an issue.

## Neovim configuration

Install the following plugins in your neovim config:
* [mason](https://github.com/williamboman/mason.nvim)
* [mason-lspconfig](https://github.com/williamboman/mason-lspconfig.nvim)
* [lspconfig](https://github.com/neovim/nvim-lspconfig)

> [!NOTE]
> Mason is optional — you can install `clangd` and `lua-language-server` via your system package manager.


I use `lazy.nvim` so, just add the following to your plugins table, or create a new file in `lua/plugins/lsp.lua`

```lua
return {
  {
    "williamboman/mason.nvim",
      config = function()
      require("mason").setup({})
    end,
  },
  {
    "williamboman/mason-lspconfig.nvim",
    config = function()
      require("mason-lspconfig").setup({ ensure_installed = { "lua_ls", "clangd" }, })
    end
  },
  {
    "neovim/nvim-lspconfig",
    config = function()
      local lspconfig = require("lspconfig")
      lspconfig.lua_ls.setup({})
      lspconfig.clangd.setup({
        cmd = { "clangd", "--background-index", },
      })
    end,
  },
}
```

## Project configuration

> [!TIP]
> You can also use this repository as a template if you are planning to use version control anyways

1. Clone this repository locally with
   ```
   $ git clone https://github.com/ironlungx/nvim-pio PROJECT_NAME/
   $ cd PROJECT_NAME
   ```

2. Change options in `platformio.ini` (stuff like `board` and `platform`)
3. `pio init --ide vim` This creates `.ccls` which `conv.py` uses to generate `compile_commands.json`
4. `rm compile_commands* && python3 conv.py` (you can also delete `compile_commands.json.bak` after this)
5. LSP should now work! If it doesn't open an issue and I will try my best to help you

> If you find a better way to get LSP working, please open a PR


## Related Project(s)
- [nvim-platformio.lua](https://github.com/anurag3301/nvim-platformio.lua)
