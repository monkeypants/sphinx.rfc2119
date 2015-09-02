Introduction
============

The purpose of this sphinx extension is enable markup of requirements per the definitions in RFC 2119. 

 * http://sphinx-doc.org
 * https://www.ietf.org/rfc/rfc2119.txt

This is supported by a suite of requirement directives that correspond to the RFC 2119 keywords. There are also a suite of requirement list directives that support documenting reqiurements (that have been defined with the rfc2119 directives).

This module is in ALPHA status. Feedback / pull requests very welcome. Development occurs on

 * https://github.com/monkeypants/sphynx.rfc2119/

Documentation is a bit strange - I used the directives to docuiment what it is supposed to do. Which was handy as I made it, but probably not very readable.

Basically, include the module then use the directives. They have lower case names.

.. must::

   As per RFC 2119, users of this module should include a block of
   boilerplate near the beginning of their sphinx document.
   A `rfc2119interpretation` directive is required for this purpose.


.. rfc2119interpretation::


.. may::

   Optionally, this module should support governance parameters for
   documenting requirement status, valid from date, review date, etc.
   
   None of these features are implemented yet, sorry. If there's
   something you actually need, please raise a ticket on GitHub.
