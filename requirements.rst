Requirements
============

The purpose of this sphinx extension is enable markup of requirements per the definitions in RFC 2119. 

.. must::

   As per RFC 2119, users of this module should include the following text near the beginning of their sphinx document.
   
       The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
       NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
       "OPTIONAL" in this document are to be interpreted as described in
       RFC 2119.

.. mandatorylist::




.. optional:

   It also (optionally) supports governance parameters for documenting requirement status, valid from date, review date.


Requirement specification directives:
 * `must` (equivalent to MUST keyword)
 * `required` (alias for `must` directive)
 * `shall` (alias for `must` directive)
 * `must_not` (equivalent to MUST NOT)
 * `shall_not` (alias for `must_not` directive)
 * `should` (equivalent to SHOULD keyword)
 * `recommended` (alias for `should` directive)
 * `should_not` (equivalent of SHOULD NOT key word)
 * `not_recommended` (alias for `should_not` directive)
 * `optional` (equivalent of OPTIONAL keyword)
 * `may` (alias for `optional` directive)

Requirement catalogue directives:
 * `mandatorylist` creates a list of all MUST (and equivalent) requirements
 * `mandatorynotlist` creates a list of all MUST NOT (and equivalent) requirements
 * `recommendedlist` creates a list of all SHOULD (and equivalent) requirements
 * `recommendednotlist` creates a list of all SHOULD NOT (and equivalent) requirements
 * `optionallist` creates a list of all OPTIONAL (and equivalent) requirements

Also, the `rfc2119interpretation` directive inserts the following text:

    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
    NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
    "OPTIONAL" in this document are to be interpreted as described in
    RFC 2119.
