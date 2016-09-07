# FontTest

This is a very early draft for what might become some day an OpenType
test suite. The purpose of this test suite is to make sure that all
OpenType implementations render fonts in a reasonably similar
way. Currently, the test suite is very much in its infancy, so please
don’t be disappointed if you don’t find much. Of course you are more
than welcome to help; just send a pull request.

```bash
$ git clone --recursive https://github.com/brawer/fonttest.git && cd fonttest
$ python check.py --output=report.html --engine=FreeStack
```


## Supported Platforms

Currently, the test suite supports only two OpenType implementations:

* With `--engine=FreeStack`, the tests are run on the free/libre
open-source text rendering stack with [FreeType](https://www.freetype.org/),
[HarfBuzz](https://www.freedesktop.org/wiki/Software/HarfBuzz/),
[FriBidi](https://www.fribidi.org/),
and [Raqm](https://github.com/HOST-Oman/libraqm). These libraries
are used by Linux, Android, ChromeOS, and many other systems.

* With `--engine=CoreText`, the tests are run on Apple’s CoreText.
This option will work only if you run the test suite on MacOS X.

* With `--engine=fontkit`, the tests are run on 
[fontkit](http://github.com/devongovett/fontkit), a JavaScript font engine.
Make sure you have [NodeJS](http://nodejs.org/) installed, and run `npm install`
prior to running the tests to install dependencies.

If you’d like to test another OpenType implementation, please go ahead.


## Generated Reports

When you pass `--output=report.html`, the test suite will generate a
test report that explains what was tested, which tests have passed,
and which ones have failed. By clicking the following links, you can
also just look at the reports
for [FreeStack](https://raw.githack.com/brawer/fonttest/master/reports/FreeStack.html)
and [CoreText](https://raw.githack.com/brawer/fonttest/master/reports/CoreText.html) without running the test suite yourself.


## Test Cases

The test cases are defined in the [testcases](testcases/) directory.
It contains HTML snippets which describe each test, and define the
rendering parameters together with the expected result.

For each test case, the `check.py` script parses the HTML snippet to
extract the rendering parameters. Then, it runs a sub-process (written
in C++ and Objective C) that writes the observed rendering in SVG
format to Standard Output. Finally, the script checks whether the
expected rendering matches the observed result.  Currently, “matching”
is implemented as exact string equality on the SVG file; if needed,
this could of course be made resilient to small rounding differences.
