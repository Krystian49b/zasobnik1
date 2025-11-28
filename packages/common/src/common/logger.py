from structlog import (
    configure,
    contextvars,
    processors,
    make_filtering_bound_logger,
    PrintLoggerFactory,
)


def configure_logging():
    configure(
        processors=[
            contextvars.merge_contextvars,
            processors.add_log_level,
            processors.TimeStamper(fmt="iso"),
            processors.CallsiteParameterAdder(
                [
                    processors.CallsiteParameter.MODULE,
                    processors.CallsiteParameter.FUNC_NAME,
                    processors.CallsiteParameter.LINENO,
                ]
            ),
            processors.JSONRenderer(),
        ],
        wrapper_class=make_filtering_bound_logger(10),
        context_class=dict,
        logger_factory=PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )
