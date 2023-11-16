# Contributing to oaipmh-scythe

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways.

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/afuetterer/oaipmh-scythe/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with [bug][bug-issues] and [help wanted][help-wanted-issues] is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with [feature][feature-issues] and [help wanted][help-wanted-issues] is open to whoever wants to implement it.

### Write Documentation

oaipmh-scythe could always use more documentation, whether as part of the official oaipmh-scythe docs, in docstrings,
or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/afuetterer/oaipmh-scythe/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome.

## Get Started!

Ready to contribute?

You need Python 3.8+ and [hatch](https://github.com/pypa/hatch). You can install it globally with [pipx](https://github.com/pypa/pipx):

```console
$ pipx install hatch
```

or locally with (this will install it in the local virtual environment):

```console
$ pip install hatch
```

Here's how to set up oaipmh-scythe for local development.

1. Fork the oaipmh-scythe repository on GitHub.
2. Clone your fork locally:
    ```console
    $ git clone git@github.com:username/oaipmh-scythe.git
    ```
3. Install your local copy into a virtual environment. Assuming you have hatch installed, this is how you set up your fork for local development:
    ```console
    $ cd oaipmh-scythe
    $ hatch shell
    $ pre-commit install
    ```
4. Create a branch for local development:
    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```
   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass pre-commit and the
   tests:
    ```console
    $ hatch run lint:all
    $ hatch run cov
    ```

6. Commit your changes and push your branch to GitHub::
    ```console
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
    ```

7. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring.
3. The pull request should work for Python >= 3.8. Check
   https://github.com/afuetterer/oaipmh-scythe/pulls
   and make sure that all the tests pass.

---

*This contributor guide is adapted from [cookiecutter-pypackage (BSD 3-Clause License)](https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/CONTRIBUTING.rst).*

<!-- Markdown links -->
[bug-issues]: https://github.com/afuetterer/oaipmh-scythe/labels/type%3A%20bug
[feature-issues]: https://github.com/afuetterer/oaipmh-scythe/labels/type%3A%20feature
[help-wanted-issues]: https://github.com/afuetterer/oaipmh-scythe/labels/help%20wanted