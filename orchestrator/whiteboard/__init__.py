"""Virtual whiteboard.

Single-user canvas: student draws something, submits a PNG, a local
vision model (qwen2.5vl:3b by default) returns a short tutor reaction
in JSON. No persistence — runs entirely in memory.
"""
