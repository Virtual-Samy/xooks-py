# XRPL Hooks Testnet

Docker Compose the xrpl testnet (Can also just change the code to connect to the public RPC)

`docker-compose up -d --build`

# Workflow

## Step 0
Make changes in `src/lib.c`

## Step 1

Build

```bash
make
```

The builded wasm hook is contained in the project root directory.

## Step 2

Set hook

```bash
python3 set_hook.py s*** hook_debug
```

## Step 3
Check

```bash
python3 pay.py s*** 1000 r***
```

## Step 4

Goto -> "Step 0" :)

## Release

[WIP] Copy from Rust Hooks Repo. Want to build 2 hooks. Debug and Release.
