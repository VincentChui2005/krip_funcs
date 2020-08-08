from .imported.treelib import Tree
import shlex


class Commander:
    def __init__(self, caller=""):
        self.caller = caller
        self.tree = Tree()

        self.tree.create_node("/", "/")

    def __call__(self, cmd:str):
        if cmd.find(self.caller) == 0:
            phrases = shlex.split(cmd)
            phrases[0] = phrases[0].split(self.caller)[1]  # Remove the caller tag in the first phrase
            phrases.insert(0, "/")  # Put the caller tag as the very first phrase

            p, a = self._split(phrases)
            return self._run(p, *a)

    # Decorator to add commands
    def command(self, name="", parent=""):
        def decorator(func):
            self._add_func(func, name, parent)
        return decorator


    def _split(self, phrases:list):
        tests = [phrases.pop(0)]
        for p in phrases:
            tests.append(tests[-1] + ":" + p)

        func_path = None
        for t in tests:
            if self.tree.get_node(t) is None:
                func_path = tests[tests.index(t)-1]
                break

        func_path = func_path or tests[-1]
        args = (tests[-1].split(func_path)[1]).split(":")[1:]

        return func_path, args

    def _run(self, func_path, *args):
        func = self.tree.get_node(func_path).data
        if func is None:
            raise Exception("function not found")
        else:
            return func(*args)

    def _add_func(self, func, name="", parent=""):
        name = name or func.__name__
        parent = "/" + ("" if parent == "" else ":" + parent)
        nid = parent + ":" + name
        self.tree.create_node(name, nid, parent, func)

