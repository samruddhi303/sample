# Virtual enviroment --->
# a virtual is a tool used to isolate specific python enviroment on a single machine ,
# allowing you to work on multiple projects with different dependencies and packages without conflicts
 

# to create a virtual env in python ,you can use the venv module that comes with python ,

# python -m venv myenv

# Activate the vitual enviroment(linux/macOS)
# source myenv/bin/activate

# Activate the virtual env (windows)
# myenv\Script\activate.bat  (activate.ps1(for powershell))

# since the virtual enviroment is activated any packages that you want to install using pip will be installed in the virtual Environment

# To deactivate the virtual enviroment 
#  deactivate