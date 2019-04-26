import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='rft',  
     version='0.1',
     scripts=['rft'] ,
     author="Christophe Bolle",
     author_email="christophe_xxx@yahoo.fr",
     description="RFT is a collection of tools and libraries around RobotFramework",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/christophettat/RFT",
     packages=setuptools.find_packages(),
     install_requires=[
          'robotframework==3.1.1',
          'robotframework-seleniumlibrary==3.3.1',
      ],
     classifiers=[
         "Programming Language :: Python :: 2",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )