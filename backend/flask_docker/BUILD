load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@io_bazel_rules_docker//container:container.bzl", "container_image")

py_library(
    name = "flask_web",
    srcs = [
        ":hello.py",
    ],
    # main = ":hello.py",
    deps = [
        "@common_pip_flask//:pkg",
    ],
)

container_image(
    name = "python_image",
    base = "@python_linux_image//image",
    symlinks = {
        "/usr/bin/python": "/usr/bin/python3",
    },
    # entrypoint = [
    #     "echo",
    #     "$PATH",
    # ],
    # files = [
    #     ":flask_web",
    # ],
    # cmd = [
    #     "python3",
    #     "hello.py",
    # ],
)

py3_image(
    name = "flask_web_image",
    base = "python_image",
    srcs = [
        "hello.py"
    ],
    main = "hello.py",
    deps = [":flask_web"],
    toolchains = [
        "//:container_py_toolchain",
    ],
)



container_image(
    name = "container_image",
    base = "@python_linux_image//image",
    files = [
        ":hello.py",
        ":flask_web",
        "//:requirements.in",
    ],
    cmd = [
        "sh",
        "-c",
        "pip3 install -r requirements.in; python3 hello.py",
    ],
)