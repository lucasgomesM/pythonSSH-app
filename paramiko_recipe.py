from pythonforandroid.recipe import PythonRecipe
class ParamikoRecipe(PythonRecipe):
    version = 'master'
    url = 'https://files.pythonhosted.org/packages/1d/08/3b8d8f1b4ec212c17429c2f3ff55b7f2237a1ad0c954972e39c8f0ac394c/paramiko-2.11.0.tar.gz'

    depends = ['python3', 'bcrypt','pynacl']

    site_packages_name = 'paramiko'

recipe = ParamikoRecipe()