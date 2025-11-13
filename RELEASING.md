# Releasing the ea


```shell
cldfbench makecldf cldfbench_gmted2010.py --with-zenodo --with-cldfreadme --glottolog-version v5.2
pytest
```

```shell
cldfbench readme cldfbench_gmted2010.py
cldfbench zenodo --communities dplace cldfbench_gmted2010.py
dplace check cldfbench_gmted2010.py
```

```shell
git status
git tag
```

Adapt CHANGELOG.md.
Add, commit and push all changes.

```shell
dplace release cldfbench_gmted2010.py vX.Y
```