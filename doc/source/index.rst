.. _overview:

.. currentmodule: econtools

.. toctree::
    :hidden:

    io.rst
    metrics.rst
    to_latex.rst
    data_manipulation.rst
    plot.rst
    reference.rst
    api.rst


****************
Package overview
****************

:mod:`econtools` is a `Python <https://www.anaconda.com/download/>`_ package for
econometrics and data manipulation.

.. contents:: :local:


Installation
------------
Download or clone ``econtools``
`here <https://github.com/dmsul/econtools>`_ and run the ``setup.py`` script::

$ python setup.py install

Requirements
++++++++++++

* Python 3.6+
* Pandas and its dependencies (Numpy, etc.)
* Scipy and its dependencies
* Pytables (optional, if you use HDF5 files)
* PyTest (optional, if you want to run the tests)


Input/Output (I/O) Tools
------------------------

:mod:`econtools` contains a number of boilerplate methods that make it easier to
create datasets, save them to disk, and prepare them for statistical analysis.

Highlights include

* :py:func:`~econtools.load_or_build`: a decorator that caches a DataFrame to disk.
* :py:func:`~econtools.save_cli`: an ``argparse`` wrapper that
  adds a ``--save`` command line switch to any script.
* :py:func:`~econtools.confirmer`: a drop-in interactive method that prompts the
  user for a yes or no response, e.g. "Are you sure you want to delete all your
  data?"

Full I/O documentation :ref:`here <io>`.

Data Manipulation Tools
-----------------------
:mod:`econtools` also contains a few helper functions that make data cleaning a
bit easier

* :py:func:`~econtools.stata_merge` wraps `pandas.merge` and adds a few
  Stata-like niceties like a flag for whether observations existed in the left,
  right, or both datasets (cf `_merge` variable in Stata).
* :py:func:`~econtools.group_id` makes it easy to generate your own arbitrary
  ID number based on a list of other variables.

Econometric Tools
-----------------

The econometrics submodule :mod:`econtools.metrics` includes

* Common regression techniques (OLS, 2SLS, LIML) with results tested against
  Stata (except where Stata has documented errors).
* Option to absorb any variable into fixed effects via within transformation.
  This is similar to the ``areg, absorb`` command in Stata but is included in
  the main regression functions. This consolidates most Stata regression
  methods into two :mod:`econtools.metrics` functions:

    * :py:func:`~econtools.metrics.reg`: ``reg``, ``areg``, ``xtreg``
    * :py:func:`~econtools.metrics.ivreg`: ``ivreg``, ``xtivreg``

  These functions also use the correct degrees of freedom corrections.
* Robust standard errors

    * robust/HC1, HC2, HC3
    * Clustered standard errors
    * Spatial HAC (aka Conley standard errors) with uniform or triangle kernel

* F-tests by variable name or arbitrary ``R`` matrix.
* Kernel density estimation
* Local linear regression
* WARNING [31 Oct 2019]: Predicted values (yhat and residuals) may not be as
  expected in transformed regressions (when using fixed effects or using
  weights). That is, the current behavior is different from Stata. I am looking
  into this and will post a either a fix or a justification of current behavior
  in the near future.

Full econometrics documentation :ref:`here <metrics>`.

LaTeX Tools
-----------

* :py:func:`~econtools.outreg` creates LaTeX table fragments from
  regression results.
* :py:func:`~econtools.table_statrow` creates bottom rows of regression tables
  (e.g., R-squared) and summary statistic tables.

Full LaTeX documentation :ref:`here <tolatex>`.


Plotting Tools
--------------

* :py:func:`~econtools.binscatter`

Full plotting tools documentation :ref:`here <plot>`.


Reference Tools
---------------

Crosswalks between U.S. state names, abbreviations, and FIPS codes, as well as
raw lists of each set of identifiers.

Full reference tools documentation :ref:`here <reference>`.
