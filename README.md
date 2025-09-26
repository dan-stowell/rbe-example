# rbe-example


## [MODULE.bazel](MODULE.bazel)
```bazel
bazel_dep(name = "toolchains_buildbuddy")
archive_override(
    module_name = "toolchains_buildbuddy",
    integrity = "sha256-VtJjefgP2Vq5S6DiGYczsupNkosybmSBGWwcLUAYz8c=",
    strip_prefix = "buildbuddy-toolchain-66146a3015faa348391fcceea2120caa390abe03",
    urls = ["https://github.com/buildbuddy-io/buildbuddy-toolchain/archive/66146a3015faa348391fcceea2120caa390abe03.tar.gz"],
)
buildbuddy = use_extension("@toolchains_buildbuddy//:extensions.bzl", "buildbuddy")

register_toolchains(
    "@toolchains_buildbuddy//toolchains/cc:ubuntu_gcc_x86_64",
)

```

## [BUILD.bazel](BUILD.bazel)
```python
load("@rules_cc//cc:defs.bzl", "cc_binary")

cc_binary(
    name = "main_cc",
    srcs = ["main.cc"],
)
```

## Build a binary locally
```sh
bazel build //:main_cc \
    --bes_results_url=https://app.buildbuddy.io/invocation/ \
    --bes_backend=grpcs://remote.buildbuddy.io \
    --experimental_platform_in_output_dir
```

## Build a binary remotely
```sh
bazel build //:main_cc \
    --bes_results_url=https://app.buildbuddy.io/invocation/ \
    --bes_backend=grpcs://remote.buildbuddy.io \
    --remote_executor=grpcs://remote.buildbuddy.io \
    --platforms=@toolchains_buildbuddy//platforms:linux_x86_64 \
    --extra_execution_platforms=@toolchains_buildbuddy//platforms:linux_x86_64 \
    --experimental_platform_in_output_dir
```
