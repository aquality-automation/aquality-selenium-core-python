"""
Appends the codecov token to the 'codecov.yml' file at the root of the repository.

This is done by CI during PRs and builds on the pytest-dev repository so we can upload coverage, at least
until codecov grows some native integration like it has with Travis and AppVeyor.
"""
import os.path
from textwrap import dedent


def main():
    this_dir = os.path.dirname(__file__)
    cov_file = os.path.join(this_dir, "..", "codecov.yml")

    assert os.path.isfile(cov_file), "{cov_file} does not exist".format(
        cov_file=cov_file
    )

    with open(cov_file, "a") as f:
        # token from: https://codecov.io/gh/aquality-automation/aquality-selenium-core-python/settings
        # use same URL to regenerate it if needed
        text = dedent(
            """
            codecov:
              token: "fba2499e-bb5b-4565-9105-76c5bf157197"
        """
        )
        f.write(text)

    print("Token updated:", cov_file)


if __name__ == "__main__":
    main()
