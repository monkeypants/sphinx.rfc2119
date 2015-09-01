# sphinx.rfc2119
sphinx extension for documenting conformance criteria per IETF RFC 2119

http://sphinx-doc.org

The purpose of this sphinx extension is enable markup of requirements per the definitions in RFC 2119. 

https://www.ietf.org/rfc/rfc2119.txt

As per RFC 2119, users of this module should include the following text near the beginning of their sphinx document.

    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
    NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
    "OPTIONAL" in this document are to be interpreted as described in
    RFC 2119.

It also (optionally) supports governance parameters for documenting requirement status, valid from date, review date.


## Examples of use

Defining a recommendation:

    .. should::
    
       :status: draft
       :review: 2015.09.30
    
       A burning widget should be self-extingushing in a dry admosphere at sea level on a hot day

Defining a mandatory requirement:

    .. must::
    
       A pile of 3 burining widgets must be readily extingusishable with a small domestic fire extingusher


## Supported Directives

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
