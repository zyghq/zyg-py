# Events
(*events*)

## Overview

### Available Operations

* [capture](#capture) - Capture a customer event

## capture

Endpoint to record a customer event with details like event type, severity, and notification flag.

### Example Usage

```python
import dateutil.parser
import zyg_py
from zyg_py import ZygPy

s = ZygPy()

res = s.events.capture(request={
    "event": "Billing Issue",
    "body": "Could not renew subscription",
    "customer": {
        "customer_id": "xxxx",
        "external_id": "ext-1234",
        "email": "customer@example.com",
    },
    "notify": True,
    "severity": zyg_py.Severity.WARNING,
    "timestamp": dateutil.parser.isoparse("2024-10-21T12:34:56Z"),
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.EventRequest](../../models/eventrequest.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostEventsResponseBody](../../models/posteventsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |