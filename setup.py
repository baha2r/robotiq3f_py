from setuptools import setup, find_packages

setup(
    name='3F_robotiq_gripper',
    version='1.0',
    packages=find_packages(),
    description='Controlling the Robotiq 3F gripper using python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Bahador Beigomi',
    author_email='baha2r@yorku.ca',
    keywords='robotiq 3f gripper',
    url='https://github.com/baha2r/robotiq_3f_gripper',
    license='Apache License 2.0',
    install_requires=[
        'pyserial',
        'numpy',
        'pymodbustcp'
    ],
    classifiers=[
        # Choose your license as you wish
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
)
