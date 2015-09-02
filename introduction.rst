Introduction
============

The purpose of this sphinx extension is enable markup of requirements per the definitions in RFC 2119. 

 * http://sphinx-doc.org
 * https://www.ietf.org/rfc/rfc2119.txt

This is supported by a suite of **requirement directives** that correspond to the RFC 2119 keywords. There are also a suite of supporting **requirement list directives**.

.. must::

   As per RFC 2119, users of this module should include a block of
   boilerplate near the beginning of their sphinx document.
   A `rfc2119interpretation` directive is required for this purpose.


... rfc2119interpretation::


.. note::

   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and OPTIONAL" in this document are to be interpreted as described in RFC 2119.


may: Optionally, this module should support governance parameters for documenting requirement status, valid from date, review date, etc.
