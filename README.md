# Android Lint to Gitlab Code Quality Report

[![PyPI version](https://badge.fury.io/py/android-lint-to-glcq.svg)](https://badge.fury.io/py/android-lint-to-glcq)

Convert android gradle lint outputs to a GitLab valid json code quality result file.

Thanks to the author of the original
project [ansible-lint-to-junit-xml](https://github.com/andreferreirav2/ansible-lint-to-junit-xml)
and to author of yaml-lint fork [yaml-lint-to-junit-xml](https://github.com/shipilovds/yaml-lint-to-junit-xml)

## Quickstart

Install `android-lint-to-glcq` with pip:

    pip install android-lint-to-glcq

Or you can simply get this repo and install with setup.py

## Usage

Run `./gradlew :app:lintDebug` and use a file to pass the output

    ./gradlew :app:lintDebug
    android-lint-to-glcq <relative path to lint xml report> <absolute path to project root> > <output file>

## Features

- Output JSON file is compliant
  with [gitlab code quality schema](https://docs.gitlab.com/ee/user/project/merge_requests/code_quality.html#implementing-a-custom-tool)
  , so you can use it to artifact as report

## Example

Running `./gradlew :app:lintDebug` on my Android project results in:

```
<?xml version="1.0" encoding="UTF-8"?>
<issues format="6" by="lint 7.0.1">

    <issue
        id="FragmentTagUsage"
        severity="Warning"
        message="Replace the &lt;fragment> tag with FragmentContainerView."
        category="Correctness"
        priority="5"
        summary="Use FragmentContainerView instead of the &lt;fragment> tag"
        explanation="FragmentContainerView replaces the &lt;fragment> tag as the preferred                 way of adding fragments via XML. Unlike the &lt;fragment> tag, FragmentContainerView                 uses a normal `FragmentTransaction` under the hood to add the initial fragment,                 allowing further FragmentTransaction operations on the FragmentContainerView                 and providing a consistent timing for lifecycle events."
        url="https://developer.android.com/reference/androidx/fragment/app/FragmentContainerView.html"
        urls="https://developer.android.com/reference/androidx/fragment/app/FragmentContainerView.html"
        errorLine1="        &lt;fragment"
        errorLine2="         ~~~~~~~~">
        <location
            file="/Users/vlad/StudioProjects/Company/fleet/app/src/main/res/layout/activity_main.xml"
            line="13"
            column="10"/>
    </issue>

</issues>
```

Running `android-lint-to-glcq` on gradle lint outputs looks line this:

    ./gradlew :app:lintDebug
    android-lint-to-glcq app/lint/reports/lint-results-debug.xml /Users/vlad/StudioProjects/Company/fleet/ > results/android-lint-results.xml

Would result in:

```
[
  {
    "description": "Use FragmentContainerView instead of the <fragment> tag",
    "severity": "major",
    "fingerprint": "f753a37f26e791db8d499657e23f9caa",
    "location": {
      "path": "fleet/app/src/main/res/layout/activity_main.xml",
      "lines": {
        "begin": "13"
      }
    }
  }
]
```

And final result:

![result](gitlab.png)

