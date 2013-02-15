Snowball stemming library collection for Python
===============================================

This document pertains to the Python version of the stemmer library distribution,
available for download from:

* https://github.com/shibukawa/snowball_jsx/

Original program is maintained at following place:

* http://snowball.tartarus.org/

Original Snowball product is created by Dr Martin Porter and  Richard Boulton (Java porting) under
BSD license.

How to use library
------------------

You can use each stemming modules from Python program.

.. code-block:: python

   import snowballstemmer

   stemmer = snowballstemmer.EnglishStemmer();
   print(stemmer.stem("We are the world"));

Following modules are common modules. Don't forget bundle these modules to your program:

* ``snowballstemmer/__init__.py``
* ``snowballstemmer/among.py``
* ``snowballstemmer/basestemmer.jsx``

Following modules are optiona modules. Select your needed language modules:

* ``danish_stemmer.py``
* ``dutch_stemmer.py``
* ``english_stemmer.py``
* ``finnish_stemmer.py``
* ``french_stemmer.py``
* ``german_stemmer.py``
* ``hungarian_stemmer.py``
* ``italian_stemmer.py``
* ``norwegian_stemmer.py``
* ``porter_stemmer.py``
* ``portuguese_stemmer.py``
* ``romanian_stemmer.py``
* ``russian_stemmer.py``
* ``spanish_stemmer.py``
* ``swedish_stemmer.py``
* ``turkish_stemmer.py``

The TestApp example
-------------------

The :file:`testapp.jsx` example program allows you to run any of the stemmers
on a sample vocabulary.

Usage::

   testapp.py <algorithm> "sentences ... "

.. code-block:: bash

   $ python testapp.py English "sentences... "

License
-------

It is a BSD licensed library.

-----------------------------

Copyright (c) 2013, Yoshiki Shibukawa

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided
that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and
  the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions
  and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

