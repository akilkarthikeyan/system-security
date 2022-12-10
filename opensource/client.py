import requests
from opentelemetry import baggage, trace
from opentelemetry.context import attach, detach
from opentelemetry.launcher import configure_opentelemetry

configure_opentelemetry(
    service_version="1.2.3",  # optional
    log_level="DEBUG",  # optional
    propagators="baggage,tracecontext",
)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("main"):
    span = trace.get_current_span()
    span.set_attribute("example", "attribute")

    # example of utilizing baggage
    ctx = baggage.set_baggage("projectID", "123")
    token = attach(ctx)

    requests.get("http://localhost:8000/hello")

    detach(token)

# set LS_ACCESS_TOKEN=a9qBFGc6Q0rEEWpdbiNXy0v6evHa33Jm+KO5FECrEGUUp0aVS0m1d2SZeoiW0clz1JSghoSfHmNl1IbB4KwGh4hN28Y6mme9IMSnZA6G
# set LS_SERVICE_NAME=client
# set OTEL_PYTHON_TRACER_PROVIDER=sdk_tracer_provider
# opentelemetry-instrument python client.py