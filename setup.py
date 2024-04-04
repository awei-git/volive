from setuptools import setup, find_namespace_packages

setup(
    name='volive',
    setuptools_git_versioning={
        "template": "{tag}",
        "dev_template": "{tag}+{branch}.{sha}",
        "dirty_tempalte": "{tag}+{branch}.{sha}.dirty",
    },
    setup_requires=['setuptools-git-versioning'],
    package_data={'volive': ['cacert.pem']},
)