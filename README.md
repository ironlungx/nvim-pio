# Neovim with PlatformIO

![screenshot](https://github.com/ironlungx/icons/blob/main/screenshot.png?raw=true)

## Overview

Since getting LSP to work is **very** finicky this guide provides **two methods** to get LSP working. Try both of them and use the one with the least errors

* **Method 1**: Using `clangd`
* **Method 2**: Using `ccls` 

> ⭐ If you find this project useful, consider starring the repo to help it gain visibility!

---

## Common Prerequisites

1. Clone the repo (if using Method 1):

```sh
git clone https://github.com/ironlungx/nvim-pio PROJECT_NAME
cd PROJECT_NAME
```

2. Set up your PlatformIO project:

* Edit `platformio.ini` to set your `board` and `platform`
* Run:

```sh
pio init --ide vim
```

---

## Method 1: Using `clangd`

### 1. Install `clangd`

Use your system package manager or install via [Mason](https://github.com/williamboman/mason.nvim)

### 2. Generate `compile_commands.json`
```sh
python3 conv.py
```

### 3. Configure Neovim LSP

Install the following Neovim plugins (using `lazy.nvim` or your preferred manager):

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
      require("mason-lspconfig").setup({
        ensure_installed = { "clangd", "lua_ls" },
      })
    end,
  },
  {
    "neovim/nvim-lspconfig",
    config = function()
      local lspconfig = require("lspconfig")
      lspconfig.lua_ls.setup({})
      lspconfig.clangd.setup({
        cmd = { "clangd", "--background-index" },
      })
    end,
  },
}
```

### 4. Run and Verify

* Open Neovim inside your project folder.
* LSP should now work. If not, feel free to open an issue.

---

## Method 2: Using `ccls` (Alternative)

### 1. Install `ccls`

Follow the install guide on [ccls GitHub](https://github.com/MaskRay/ccls/wiki/Build)

### 2. Initialize Your Project

Run:

```sh
pio init --ide vim
pio run -t compiledb
```

### 3. Configure Neovim to Use `ccls`

In your Neovim config:

```lua
vim.lsp.config("ccls", {
  init_options = {
    diagnostics = {
      onChange = 100,
    },
  },
})

vim.lsp.enable("ccls")

-- Optional: Fallback to clangd if .ccls doesn't exist
if vim.fn.filereadable(vim.uv.cwd() .. "/.ccls") == 0 then
  vim.lsp.enable("clangd")
end
```

### 4. Keep It Up to Date

Every time you modify project libraries or config:

```sh
pio init --ide vim && pio run -t compiledb
```

---

## Switching Between `clangd` and `ccls`

* Use **clangd** if you're looking for easier setup and performance.
* Use **ccls** if you prefer `.ccls`-based workflows or have specific compatibility needs.

---

## Related Projects

* [nvim-platformio.lua](https://github.com/anurag3301/nvim-platformio.lua)

> Found a better way or improvement? Open a PR or issue!
