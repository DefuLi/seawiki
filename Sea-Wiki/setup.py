from setuptools import setup, find_packages

setup(
    name = "seawiki",
    version = "2019.10.26.2",
    description = "Input any question or text, search wikipedia for the most similar documents.",

    url = "https://github.com/DefuLi/Sea-Wiki",
    author = "defuli",
    author_email = "defuli.go@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['joblib==0.14.0', 'numpy==1.16.2', 'pkg-resources==0.0.0', 'regex==2019.8.19', 'scikit-learn==0.21.3', 'scipy==1.3.1', 'sklearn==0.0']
)
