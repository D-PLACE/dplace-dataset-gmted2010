from setuptools import setup


setup(
    name='cldfbench_gmted2010',
    py_modules=['cldfbench_gmted2010'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'dplace-dataset-gmted2010=cldfbench_gmted2010:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
