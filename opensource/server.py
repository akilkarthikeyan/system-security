
from fastapi import FastAPI,Path
from opentelemetry import trace, baggage
from time import sleep
from opentelemetry.launcher import configure_opentelemetry

PORT = 8000

app = FastAPI(__name__)
tracer = trace.get_tracer(__name__)

configure_opentelemetry(
    service_version="4.5.6",
    log_level="DEBUG",  # optional
    propagators="baggage,tracecontext",
)


@app.route("/hello")
def hello():

    # get the current span, created by flask instrumentation
    current_span = trace.get_current_span()

    # add more attributes to the server span
    current_span.set_attribute("http.route", "some_route")

    # pretend to do work and record the latency
    sleep(20 / 1000)

    with tracer.start_as_current_span("server_span") as span:

        # add a baggage value
        span.set_attribute("projectID", baggage.get_baggage("projectID"))

        # add an event
        span.add_event("event message", {"event_attributes": 1})

        # pretend to do work and record the latency
        sleep(30 / 1000)

        # record an exception
        try:
            1 / 0
        except ZeroDivisionError as error:
            span.record_exception(error)
            print("caught zero division error")

        return "hello"


# set LS_ACCESS_TOKEN=POTGO9PLNhGz4VUKyAxirxlaH2/7fia+Uv26Jbxyp+1BgbCbEMhfPQSICyG5LD4/bmFQwSwm9TFno3X10Q8dL33XBKIhz2x4EZ95Vzsr
# set LS_SERVICE_NAME=server
# set OTEL_PYTHON_TRACER_PROVIDER=sdk_tracer_provider
# opentelemetry-instrument python server.py