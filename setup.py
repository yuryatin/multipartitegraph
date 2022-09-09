from distutils.core import setup

setup(
    name = 'multipartitegraph',
    packages = ['multipartitegraph'],
    version = '0.0.3',
    license = 'MIT',
    description = 'This package draws multipartite graph with fixed levels from a list of matrix dataframes',
    url = 'https://github.com/yuryatin/multipartitegraph',
    download_url = 'https://github.com/yuryatin/multipartitegraph/archive/refs/tags/v0.0.3.tar.gz',
    keywords = ['multipartite', 'graph', 'fixed', 'levels', 'plotting'],
    classifiers = [],
    install_requires = ['numpy','pandas','matplotlib']
)