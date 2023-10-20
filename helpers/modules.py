import os
import os.path
from importlib.machinery import SourceFileLoader
from types import ModuleType

class Module:
    filename: str
    name: str
    enabled: bool
    module: ModuleType

    def __init__(self, filename: str):
        self.filename = filename
        if filename.endswith(".disabled"):
            self.enabled = False
        else:
            self.enabled = True
        self.module = SourceFileLoader(filename.removesuffix(".py.disabled").removesuffix(".py"), os.path.join('modules', self.filename)).load_module()
        assert hasattr(self.module, 'geobomber_module') and self.module.geobomber_module == True, "Invalid module."
        assert hasattr(self.module, 'geobomber_module_name'), "Invalid module."
        assert hasattr(self.module, 'geobomber_module_countrycodes'), "Invalid module."
        assert hasattr(self.module, 'geobomber_module_author'), "Invalid module."
        assert hasattr(self.module, 'send_sms'), "Invalid module."
        assert hasattr(self.module, 'retry_at'), "Invalid module."
        assert hasattr(self.module, 'can_retry'), "Invalid module."
        self.name = self.module.geobomber_module_name

modules_list: list[Module] = []

def reload_modules():
    global modules_list
    modules_list = []
    for file in os.listdir(path=os.path.join(os.getcwd(), 'modules')):
        if os.path.isfile(os.path.join(os.getcwd(), 'modules', file)):
            try:
                modules_list.append(Module(file))
            except AssertionError:
                print(f"ModuleLoadError: {file}")
