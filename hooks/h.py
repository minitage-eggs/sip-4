import os
import subprocess

def h(options, buildout, version, opts):
    """Patch Makefile to point to our site packages."""
    cwd = os.getcwd()
    md = options['compile-directory']
    c = os.path.join(md, 'configure.py')
    os.chdir(md)
    p = buildout['p'][version]
    opts = ' '.join(opts.split())
    cmd = [p, c, opts]
    print "Running: %s" % ' '.join(cmd)
    ret = os.system(' '.join(cmd))
    if ret > 0: raise Exception,('Cannot confiure')
    os.chdir(cwd)

def h_24(options,buildout):
    """Patch Makefile to point to our site packages."""
    h(options, buildout, '24', options['configure-options'])
def h_25(options,buildout):
    """Patch Makefile to point to our site packages."""
    h(options, buildout, '25', options['configure-options'])
def h_26(options,buildout):
    """Patch Makefile to point to our site packages."""
    h(options, buildout, '26', options['configure-options'])
def h_27(options,buildout):
    """Patch Makefile to point to our site packages."""
    h(options, buildout, '27', options['configure-options']) 
# vim:set ts=4 sts=4 et  :
