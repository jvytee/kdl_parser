import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(name='kdl_parser_jvytee',
                 version='0.1',
                 author='Julian Theis',
                 author_email='jlntheis@gmail.com',
                 description='Create PyKDL chains from URDF robot descriptions',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 url='https://github.com/jvytee/kdl_parser',
                 packages=setuptools.find_packages(),
                 classifiers=['Programming Language :: Python :: 3',
                              'License :: OSI Approved :: BSD License',
                              'Operating System :: OS Independent'])
