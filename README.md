# rbe-example


This [MODULE.bazel] snippet
```python
bazel_dep(name = "toolchains_buildbuddy")
archive_override(
    module_name = "toolchains_buildbuddy",
    integrity = "sha256-VtJjefgP2Vq5S6DiGYczsupNkosybmSBGWwcLUAYz8c=",
    strip_prefix = "buildbuddy-toolchain-66146a3015faa348391fcceea2120caa390abe03",
    urls = ["https://github.com/buildbuddy-io/buildbuddy-toolchain/archive/66146a3015faa348391fcceea2120caa390abe03.tar.gz"],
)
buildbuddy = use_extension("@toolchains_buildbuddy//:extensions.bzl", "buildbuddy")
buildbuddy.platform(buildbuddy_container_image = "UBUNTU20_04_IMAGE")

register_toolchains(
    "@toolchains_buildbuddy//toolchains/cc:ubuntu_gcc_x86_64",
    "@toolchains_buildbuddy//toolchains/cc:ubuntu_gcc_arm64",
    "@toolchains_buildbuddy//toolchains/cc:windows_msvc_x86_64",
)
```

and [BUILD.bazel] snippet
```python
load("@rules_cc//cc:defs.bzl", "cc_binary")

cc_binary(
    name = "main_cc",
    srcs = ["main.cc"],
)
```

lets you build a Linux x86_64 binary with this command:
```bash
bazel build //:main_cc --remote_executor=grpcs://remote.buildbuddy.io --host_platform=@toolchains_buildbuddy//platforms:linux_x86_64
```
