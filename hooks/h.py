import os
import sys
import os
import sys
import subprocess
def which(program, environ=None, key = 'PATH', split = ':'):
    if not environ:
        environ = os.environ
    PATH=environ.get(key, '').split(split)
    for entry in PATH:
        fp = os.path.abspath(os.path.join(entry, program))
        if os.path.exists(fp):
            return fp
        if (sys.platform.startswith('win') or sys.platform.startswith('cyg'))  and os.path.exists(fp+'.exe'):
            return fp+'.exe'
    raise IOError('Program not fond: %s in %s ' % (program, PATH)) 




from distutils.sysconfig import get_python_lib


def h(options, buildout, opts):
    """Patch Makefile to point to our site packages."""
    cwd = os.getcwd()
    md = options['compile-directory']
    c = os.path.join(md, 'configure.py')
    os.chdir(md)
    opts = ' '.join(opts.split())
    py = buildout['buildout']['executable']
    if not  py.startswith('/'):
        py = which(py)
    includes = os.path.join(sys.prefix, 'includes')
    lib = os.path.join(sys.prefix, 'lib')
    sp = get_python_lib()
    sip = os.path.join(get_python_lib(), 'sip')
    bins = os.path.join(sys.prefix, 'bin')
    opts = '-b %s -d %s -e %s -v %s' % (
        bins, sp, includes, sip)
    cmd = [py, c, opts]
    print "Running: %s" % ' '.join(cmd)
    ret = os.system(' '.join(cmd))
    if ret > 0: raise Exception,('Cannot confiure')
    os.chdir(cwd)

def h_27(options,buildout):
    """Patch Makefile to point to our site packages."""
    h(options, buildout, options['configure-options']) 
# vim:set ts=4 sts=4 et  :
