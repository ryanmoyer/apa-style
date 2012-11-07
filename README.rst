The following code is another Test-Driven Development exercise for
`Mott Fisk`_ and `Ryan Moyer`_.

The purpose of the program is to format a reference for a reference
list according to the `APA citation style`_ given the necessary
informtation about it. `Son of Citation Machine`_ is an example of a web application which does this.

.. _Mott Fisk: https://github.com/mottfisk
.. _Ryan Moyer: https://github.com/ryanmoyer
.. _APA citation style: http://www.library.cornell.edu/resrch/citmanage/apa
.. _Son of Citation Machine: http://citationmachine.net/index2.php

=========
 Purpose
=========

* Practice ``git`` skills.
* Practice skills developing using TDD.
* Practice formatting skills.
* Learn how to use exceptions in Python.

==============
 Instructions
==============

* Log in to your GitHub account.
* Fork my repository by following GitHub's guide to `Forking a Repo`_.
* Clone the code from your new repository using the GitHub client.
* Run the test suite by running ``python test_apa.py`` on the command-line. All tests should fail.
* Complete the code in ``apa.py`` such that it passes all the
  tests. I will help you on the tests that expect errors to be raised.
* Add extra tests if desired!
* Commit the code locally.
* Sync the code to your repository.
* Submit a `pull request`_ to my original repository. I will help you on this.

.. _Forking a Repo: https://help.github.com/articles/fork-a-repo
.. _pull request: https://help.github.com/articles/using-pull-requests

=======
 Notes
=======

The tests cases for this program don't technically follow strict APA
style. You shouldn't need to consult an APA manual to make it
work. Just look at the tests and make them pass.

=======
 Hints
=======

* You are required to use `str.format()`_ to do the formatting
  code. You may want to use the keyword argument form instead of the
  positional argument form. Ask me about it or attempt to figure it
  out on your own.
* You'll want to use `str.split()`_ to correctly handle the full names.
* Look in the tutorial sections `Errors and Exceptions`_ if you'd like
  to learn how they work, specifically `Raising Exceptions`_.

.. _str.format(): http://docs.python.org/2/library/stdtypes.html?highlight=format#str.format
.. _str.split(): http://docs.python.org/2/library/stdtypes.html?highlight=split#str.split
.. _Errors and Exceptions: http://docs.python.org/2/tutorial/errors.html
.. _Raising Exceptions: http://docs.python.org/2/tutorial/errors.html#raising-exceptions
