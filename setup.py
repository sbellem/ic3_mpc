from setuptools import setup


dev_require = [
    'ipdb',
    'ipython',
]

setup(
    name='mpc',
    version='0.0.1',
    py_modules=['number_shoot_out'],
    install_requires=['viff>=2.0'],
    extras_require={'dev': dev_require},
    dependency_links=[
        'git+https://github.com/sbellem/viff.git@setup#egg=2.0',
    ],
)
