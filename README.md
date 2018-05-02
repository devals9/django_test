# django_test
Test Django Python 3 project

## Getting started
This is a test python and django project based on Django Getting started guide

## Prerequisites
* Install Java
* Install Eclipse
       * Get Pydev for Eclipse
       
   
## Installation
 
### On Mac
 
 * Install Xcode
 * Install Homebrew
 * Get Python 3
 * Get virtualenv
        * pip3 install virtualenv
        * Goto django_test (project_folder)
        * virtualenv django_test  -p python3.6
        * source bin/activate   
        * pip3 install django==2.0.4
        * Refer [here](https://www.codingforentrepreneurs.com/blog/install-django-on-mac-or-linux/)
 * Setup Python Interpreter in eclipse
        * Go to Window -> Preferences -> Interpreter Python and create a new interpreter. Select the python wrapper from the virtual environment ($WORKON_HOME/YOUR_PROJECT/bin/python). The libraries should be selected automatically - leave them as they are.
        * In the project properties change the interpreter to use the newly created one (Project -> Properties -> PyDev Python Interpreter)
        * Alternatively you can manage the environment individually for each run configuration in the 'Run -> Run configurations -> Interpreter' tab
        * Link [here](http://www.michaelpollmeier.com/eclipse-pydev-and-virtualenv)
        
## Running the tests

New test files should start with test  <BR/>

To run the tests, Right click project -> Django -> Run Django Tests

## Github

## Deployment

## Tutorials

[Django tutorial](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)

  
       