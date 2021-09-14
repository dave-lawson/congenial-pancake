This implements an extremely simple API that accepts a POST/PUT request at
the URL /api/echo, expecting a JSON format payload and MIME type and returns
the same JSON data structure with a top level element "echoed" set to true.
It only will set the "echoed" element if it does not already exist and is not
already true.  It should reject non-JSON payloads and non-POST requests with a
400 Bad Request status code.

It exposes a metrics endpoint at /metrics, if this is run in a production
ready server, the metrics code will need to be updated to reflect the new
server configuration.

Currently the API is driven by the built in werkzeug server in flask, a
series of tests of the popular WSGI servers indicates that while the built in
server is slow, it's not so slow as to make it unuseful for proof of concept type
applications. Benchmarks are here: 
https://towardsdatascience.com/a-flask-full-of-whiskey-wsgi-e89525d6f9da

There is a basic test suite that covers most of the major cases for the API
that can be run via `make test` from the top level of the repository. The
Makefile also includes a lint target, `make lint` that will run pyflakes
against the python files in the repo.

A basic Docker image can be built with `make docker-build` and run with the
`make docker-run` target.
