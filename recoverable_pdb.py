import pdb
import copy
import sys


def try_copy(data):
    # some inner structure use dict or list.
    if isinstance(data, dict) or isinstance(data, list):
        ret = {}
        for i in data:
            new_copy = try_copy(data[i])
            if new_copy:
                ret[i] = new_copy
        return ret
    else:
        try:
            # copy data
            return copy.deepcopy(data)
        except Exception as e:
            # if the data can't be copied
            pass 
    # just return data.
    return data 



class RecoverablePdb(pdb.Pdb):
    def __init__(self, *args, **kwargs):
        pdb.Pdb.__init__(self, *args, **kwargs)
        self.snapshot = {}

    def do_save(self, arg):
        backup_locals = try_copy(self.curframe_locals)
        lineno = self.curframe.f_lineno
        self.snapshot[arg] = (backup_locals, lineno)

    def do_restore(self, arg):
        print self.snapshot
        if arg not in self.snapshot:
            print 'no such name'
            return
        if not self.jump_to(self.snapshot[arg][1]):
            print 'can not jump'
            return

        self.restore_env(self.snapshot[arg][0])

    def restore_env(self, env):
        # some variable is defined latter.
        # so we need to delete it if we restore runtime env.
        need_to_delete = []
        for i in self.curframe_locals:
            if i not in env:
                need_to_delete.append(i)
            else:
                self.curframe_locals[i] = env[i]
        for i in need_to_delete:
            del self.curframe_locals[i]

    def jump_to(self, arg):
        if self.curindex + 1 != len(self.stack):
            print >>self.stdout, "*** You can only jump within the bottom frame"
            return False
        try:
            arg = int(arg)
        except ValueError:
            print >>self.stdout, "*** The 'jump' command requires a line number."
            return False
        else:
            try:
                # Do the jump, fix up our copy of the stack, and display the
                # new position
                self.curframe.f_lineno = arg
                self.stack[self.curindex] = self.stack[self.curindex][0], arg
                self.print_stack_entry(self.stack[self.curindex])
            except ValueError, e:
                print >>self.stdout, '*** Jump failed:', e
                return False
        return True


def set_trace():
    RecoverablePdb().set_trace(sys._getframe().f_back)


