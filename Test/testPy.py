import sys
import os
import time
import winreg
import ctypes

def find_python():
    """
    retrieves the commandline for .py extensions from the registry
    """
    hKey = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,
                           r'Python.File\shell\open\command')
    # get the default value
    value, typ = winreg.QueryValueEx (hKey, None)
    program = value.split('"')[1]
    if not program.lower().endswith(r'\python.exe'):
        return None
    return os.path.dirname(program)


te = find_python()
print(te)


def extend_path(pypath, remove=False, verbose=0, remove_old=True,
                script=False):
    """
    extend(pypath) adds pypath to the PATH env. variable as defined in the
    registry, and then notifies applications (e.g. the desktop) of this change.
    !!! Already opened DOS-Command prompts are not updated. !!!
    Newly opened prompts will have the new path (inherited from the
    updated windows explorer desktop)
    options:
    remove (default unset), remove from PATH instead of extend PATH
    remove_old (default set), removes any (old) python paths first
    script (default unset), try to add/remove the Scripts subdirectory
        of pypath (pip, easy_install) as well
    """
    _sd = 'Scripts' # scripts subdir
    hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE,
               r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
               0, winreg.KEY_READ | winreg.KEY_SET_VALUE)

    value, typ = winreg.QueryValueEx (hKey, "PATH")
    vals = value.split(';')
    assert isinstance(vals, list)
    if not remove and remove_old:
        new_vals = []
        for v in vals:
            pyexe = os.path.join(v, 'python.exe')
            if v != pypath and os.path.exists(pyexe):
                if verbose > 0:
                    print ('removing from PATH:', v)
                continue
            if script and v != os.path.join(pypath, _sd) and \
               os.path.exists(v.replace(_sd, pyexe)):
                if verbose > 0:
                    print ('removing from PATH:', v)
                continue
            new_vals.append(v)
        vals = new_vals
    if remove:
        try:
            vals.remove(pypath)
        except ValueError:
            if verbose > 0:
                print ('path element', pypath, 'not found')
            return
        if script:
            try:
                vals.remove(os.path.join(pypath, _sd))
            except ValueError:
                pass
            print ('removing from PATH:', pypath)
    else:
        if pypath in vals:
            if verbose > 0:
                print ('path element', pypath, 'already in PATH')
            return
        vals.append(pypath)
        if verbose > 1:
            print ('adding to PATH:', pypath)
        if script:
            if not pypath + '\\Scripts' in vals:
                vals.append(pypath + '\\Scripts')
            if verbose > 1:
                print ('adding to PATH:', pypath + '\\Scripts')
    winreg.SetValueEx(hKey, "PATH", 0, typ, ';'.join(vals) )
    winreg.SetValueEx(hKey, "OLDPATH", 0, typ, value )
    winreg.FlushKey(hKey)
    # notify other programs
    SendMessage = ctypes.windll.user32.SendMessageW
    HWND_BROADCAST = 0xFFFF
    WM_SETTINGCHANGE = 0x1A
    SendMessage(HWND_BROADCAST, WM_SETTINGCHANGE, 0, u'Environment')
    if verbose > 1:
        print ('Do not forget to restart any command prompts')

if __name__ == '__main__':
    remove = '--remove' in sys.argv
    script = '--noscripts' not in sys.argv
    extend_path(find_python(), verbose=2, remove=remove, script=script)
