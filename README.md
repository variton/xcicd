# `Xcicd`

> High level features for CI/CD GitHub workflows

`Xcicd` provides a modern set of utilities CI/CD workflows.

---

## Clone repository
*remark:*
    *make sure your ssh key was added to you github account*

```
git clone git@github.com:variton/xcicd.git 
```

---

## Environment to develop the `Xcicd`
*remark:*
    *make sure you have the rights to pull the docker image*

```
docker pull ghcr.io/variton/ixcicd:1.0
```

### Set the python path
Set up the following environment variable.
Once you've cd in the root project's directory:

```
export PYTHONPATH=$PWD/src
```

### Run all the tests
*remark:*
    *make sure to use the ixpylib docker image*

Execute the following cli:

```
pytest tests
```
