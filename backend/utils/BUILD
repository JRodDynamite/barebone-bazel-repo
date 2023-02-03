load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "utils",
    srcs = glob([
        "**/*.py",
    ]),
    imports = ["src"],
    visibility = [
        "//visibility:public",
    ],
)

py_library(
    name = "utils_broken",
    srcs = glob([
        "**/*.py",
    ]),
    visibility = [
        "//visibility:public",
    ],
)