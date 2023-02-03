load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        "@common_pip_requests//:pkg",
        "//backend/utils:utils",
        # "//backend/utils:utils_broken",
    ]
)
