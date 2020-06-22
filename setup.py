from setuptools import setup


def main():
    setup(use_scm_version={"write_to": "aquality_selenium_core/_version.py"})


if __name__ == "__main__":
    main()
