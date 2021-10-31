# XRPL Hooks Testnet

# Set up env

Spin up Hooks Node

`docker-compose up -d --build`

Virtual Env & Install

```python
mkvirtualenv xooks-py \
&& pip3 install -r requirements.txt
```

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

## TODO

- Build Debug and Release hook
