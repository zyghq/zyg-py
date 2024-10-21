# Customer


## Fields

| Field                             | Type                              | Required                          | Description                       | Example                           |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `customer_id`                     | *str*                             | :heavy_check_mark:                | Internal customer ID              | xxxx                              |
| `external_id`                     | *Optional[str]*                   | :heavy_minus_sign:                | External system ID, if applicable | ext-1234                          |
| `email`                           | *Optional[str]*                   | :heavy_minus_sign:                | Email address of the customer     | customer@example.com              |