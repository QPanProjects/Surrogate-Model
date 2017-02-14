Installation
============

Requirements
------------

SurrogateModel is compatible with Python 2.

The most basic features of SurrogateModel requires Python 2.6. In order to combine the
toolbox and the multiprocessing module Python 2.7 is needed for its support to
pickle partial functions.

The computation distribution requires SCOOP_.

CMA-ES requires Numpy_, and we recommend matplotlib_ for visualization of
results as it is fully compatible with DEAP's API.

.. _SCOOP: http://www.pyscoop.org/
.. _Numpy: http://www.numpy.org/
.. _matplotlib: http://www.matplotlib.org/


Install SurrogateModel
----------------------

We encourage you to use easy_install_ or pip_ to install SurrogateModel on your system.
Linux package managers like apt-get, yum, etc. usually provide an outdated
version. ::

   easy_install SurrogateModel

or ::

   pip install SurrogateModel

If you wish to build from sources, download_ or clone_ the repository and type::

   python setup.py install

.. _download: https://pypi.python.org/pypi/deap/
.. _clone: https://github.com/SurrogateModel/SurrogateModel.git

.. _easy_install: http://pythonhosted.org/distribute/easy_install.html
.. _pip: http://www.pip-installer.org/en/latest/
