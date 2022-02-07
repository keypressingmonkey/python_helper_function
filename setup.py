import setuptools

setuptools.setup(
    name='helperfunctions',
    version='0.0.13',
    author='KeypressingMonkey',
    author_email='keypressingmonkey@web.de',
    description='Commonly reused functions',
    url='https://github.com/keypressingmonkey/python_helper_function',
    license='MIT',
    packages=['helper_functions'],
    install_requires=['requests','Pillow','Selenium','webdriver_manager'],
)