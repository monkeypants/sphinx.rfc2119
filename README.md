# sphinx.rfc2119

The purpose of this sphinx extension is enable markup of requirements per the definitions in RFC 2119.

 * http://sphinx-doc.org
 * https://www.ietf.org/rfc/rfc2119.txt

This is supported by a suite of requirement directives that correspond to the RFC 2119 keywords. There are also a suite of requirement list directives that support documenting reqiurements (that have been defined with the rfc2119 directives).

This module is in ALPHA status. Feedback / pull requests very welcome. Development occurs on GitHub:

 * https://github.com/monkeypants/sphinx.rfc2119/

Documentation is a bit strange - I used the directives to document what it is supposed to do. Which was handy as I made it, but probably not very readable.

Basically, add the module to your the conf.py of your repo then use the directives. They have lower case names.


## Alternatives

This sphinx extention is very simple, like RFC 2119.

If you want a more complex graph of requirement types,
perhaps https://sphinx-needs.readthedocs.io/ will suit you better.