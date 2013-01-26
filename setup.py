from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import numpy

## \file setup.py setup.py
#  \brief The python script for building proteus
#
#  Set the DISTUTILS_DEBUG environment variable to print detailed information while setup.py is running.
#
try:
    import sys,os.path
    sys.path.insert(0,os.path.join(sys.prefix,'proteusConfig'))
    from config import *
except:
    raise RuntimeError("Missing or invalid config.py file. See proteusConfig for examples")

###to turn on debugging in c++
##\todo Finishing cleaning up setup.py/setup.cfg, config.py...
from distutils import sysconfig
cv = sysconfig.get_config_vars()
cv["OPT"] = cv["OPT"].replace("-g","")
cv["CFLAGS"] = cv["CFLAGS"].replace("-g","")


setup(name='proteus_mprans',
      version='0.9.0',
      description='Proteus modules for simulating free surface fluid/structure interaction',
      author='Chris Kees',
      author_email='christopher.e.kees@usace.army.mil',
      url='https://adh.usace.army.mil/proteus',
      packages=['proteus.mprans'],
      package_dir={'proteus.mprans':'src'},
      ext_package='proteus.mprans',
      cmdclass = {'build_ext':build_ext},
      ext_modules=[Extension("cNCLS",["src/cNCLS.pyx"],depends=["src/NCLS.h"], language="c++",include_dirs=[numpy.get_include(),os.getenv('PROTEUS')+'/proteusModule/include',os.getenv('PROTEUS')+'/proteusModule/src']),
                   Extension("cMCorr",["src/cMCorr.pyx"],depends=["src/MCorr.h"], define_macros=[('PROTEUS_LAPACK_H',PROTEUS_LAPACK_H),
                                            ('PROTEUS_LAPACK_INTEGER',PROTEUS_LAPACK_INTEGER),
                                            ('PROTEUS_BLAS_H',PROTEUS_BLAS_H)],language="c++",include_dirs=[numpy.get_include(),os.getenv('PROTEUS')+'/proteusModule/include',os.getenv('PROTEUS')+'/proteusModule/src'],
                             library_dirs=[PROTEUS_LAPACK_LIB_DIR,
                                           PROTEUS_BLAS_LIB_DIR],
                             libraries=['m',PROTEUS_LAPACK_LIB,PROTEUS_BLAS_LIB],
                             extra_compile_args=PROTEUS_EXTRA_COMPILE_ARGS,
                             extra_link_args=PROTEUS_EXTRA_LINK_ARGS),
                   Extension("cRANS2P",["src/cRANS2P.pyx"],
		             depends=["src/RANS2P.h",os.getenv('PROTEUS')+'/proteusModule/include/ModelFactory.h',os.getenv('PROTEUS')+'/proteusModule/src/CompKernel.h'],
			     language="c++",
			     include_dirs=[numpy.get_include(),os.getenv('PROTEUS')+'/proteusModule/include',os.getenv('PROTEUS')+'/proteusModule/src']),
                   Extension("cRDLS",["src/cRDLS.pyx"],
		             depends=["src/RDLS.h",os.getenv('PROTEUS')+'/proteusModule/include/ModelFactory.h',os.getenv('PROTEUS')+'/proteusModule/src/CompKernel.h'], 
		             language="c++",
			     include_dirs=[numpy.get_include(),os.getenv('PROTEUS')+'/proteusModule/include',os.getenv('PROTEUS')+'/proteusModule/src']),
                   Extension("cVOF",["src/cVOF.pyx"],
		             depends=["src/VOF.h",os.getenv('PROTEUS')+'/proteusModule/include/ModelFactory.h',os.getenv('PROTEUS')+'/proteusModule/src/CompKernel.h'], 
		             language="c++",
			     include_dirs=[numpy.get_include(),os.getenv('PROTEUS')+'/proteusModule/include',os.getenv('PROTEUS')+'/proteusModule/src']),
                   Extension("cMoveMesh",["src/cMoveMesh.pyx"],
		             depends=["src/MoveMesh.h",os.getenv('PROTEUS')+'/proteusModule/include/ModelFactory.h',os.getenv('PROTEUS')+'/proteusModule/src/CompKernel.h'], 
		             language="c++",
			     include_dirs=[numpy.get_include(),os.getenv('PROTEUS')+'/proteusModule/include',os.getenv('PROTEUS')+'/proteusModule/src']),
                   Extension("cSW2D",["src/cSW2D.pyx"],
		             depends=["src/SW2D.h",os.getenv('PROTEUS')+'/proteusModule/include/ModelFactory.h',os.getenv('PROTEUS')+'/proteusModule/src/CompKernel.h'], 
		             language="c++",
			     include_dirs=[numpy.get_include(),os.getenv('PROTEUS')+'/proteusModule/include',os.getenv('PROTEUS')+'/proteusModule/src'],
                             extra_compile_args=PROTEUS_EXTRA_COMPILE_ARGS+['-g'],
                             extra_link_args=PROTEUS_EXTRA_LINK_ARGS+['-g']),
                   Extension("cSW2DCV",["src/cSW2DCV.pyx"],
		             depends=["src/SW2DCV.h",os.getenv('PROTEUS')+'/proteusModule/include/ModelFactory.h',os.getenv('PROTEUS')+'/proteusModule/src/CompKernel.h'], 
		             language="c++",
			     include_dirs=[numpy.get_include(),os.getenv('PROTEUS')+'/proteusModule/include',os.getenv('PROTEUS')+'/proteusModule/src'],
                             extra_compile_args=PROTEUS_EXTRA_COMPILE_ARGS+['-g'],
                             extra_link_args=PROTEUS_EXTRA_LINK_ARGS+['-g']),
                   ],
      requires=['numpy']
      )
