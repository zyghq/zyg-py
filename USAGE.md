<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import dateutil.parser
import zyg_py
from zyg_py import ZygPy

async def main():
    s = ZygPy()
    res = await s.events.capture_async(request={
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

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->