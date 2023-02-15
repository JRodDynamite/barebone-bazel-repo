load("@rules_python//python:pip.bzl", "compile_pip_requirements")

# This rule adds a convenient way to update the requirements file.
compile_pip_requirements(
    name = "requirements",
    extra_args = [
        # For installing setuptools
        "--allow-unsafe",
        # Removing warning, future proofing
        "--resolver=backtracking",
    ],
    requirements_in = "requirements.in",
    requirements_txt = "requirements_lock.txt",
)

exports_files(["requirements.in"])

load("@bazel_tools//tools/python:toolchain.bzl", "py_runtime_pair")

package(default_visibility = ["//visibility:public"])

py_runtime(
    name = "default_container_py3_runtime",
    interpreter_path = "/usr/bin/python3",
    python_version = "PY3",
)

py_runtime_pair(
    name = "default_container_py_runtime_pair",
    py2_runtime = "None",
    py3_runtime = ":default_container_py3_runtime",
)

# A toolchain to run python outputs inside a container.
# If you are using a custom base for py_image which has python tools in a
# different location, you must register that toolchain prior to the
# registration of this one in @io_bazel_rules_docker//python:image.bzl
toolchain(
    name = "container_py_toolchain",
    exec_compatible_with = [
        "@io_bazel_rules_docker//platforms:run_in_container",
    ],
    toolchain = ":default_container_py_runtime_pair",
    toolchain_type = "@bazel_tools//tools/python:toolchain_type",
)
