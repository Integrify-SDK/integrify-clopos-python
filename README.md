# Integrify Clopos

> [!Caution]
> Integrify is unofficial library, even though it is based on official documentation.

<p align="center">
  <a href="https://integrify.mmzeynalli.dev/"><img width="400" src="https://raw.githubusercontent.com/Integrify-SDK/integrify-docs-python/main/docs/az/docs/assets/integrify.png" alt="Integrify"></a>
</p>
<p align="center">
    <em>Integrify is a library that simplifies API integrations. This library is designed for Clopos integration.</em>
</p>
<p align="center">
<a href="https://github.com/Integrify-SDK/integrify-clopos-python/actions/workflows/test.yml" target="_blank">
    <img src="https://github.com/Integrify-SDK/integrify-clopos-python/actions/workflows/test.yml/badge.svg?branch=main" alt="Test">
</a>
<a href="https://github.com/Integrify-SDK/integrify-clopos-python/actions/workflows/publish.yml" target="_blank">
    <img src="https://github.com/Integrify-SDK/integrify-clopos-python/actions/workflows/publish.yml/badge.svg" alt="Publish">
</a>
<a href="https://pypi.org/project/integrify-clopos" target="_blank">
  <img src="https://img.shields.io/pypi/v/integrify-clopos?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://app.netlify.com/sites/integrify-docs/deploys">
  <img src="https://api.netlify.com/api/v1/badges/d8931b6a-80c7-41cb-bdbb-bf6ef5789f80/deploy-status" alt="Netlify Status">
</a>
</p>
<p align="center">
<a href="https://pepy.tech/project/integrify-clopos" target="_blank">
  <img src="https://static.pepy.tech/badge/integrify-clopos" alt="Downloads">
</a>
<a href="https://pypi.org/project/integrify-clopos" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/integrify-clopos.svg?color=%2334D058" alt="Supported Python versions">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/Integrify-SDK/integrify-clopos-python" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/Integrify-SDK/integrify-clopos-python.svg" alt="Coverage">
</a>

</p>

---

**Documentation**: [https://integrify.mmzeynalli.dev/integrations/clopos/about/](https://integrify.mmzeynalli.dev/integrations/clopos/about/)

**Source code**: [https://github.com/Integrify-SDK/integrify-clopos-python](https://github.com/Integrify-SDK/integrify-clopos-python)

---

## Official Documentation (v1.0.1)

[English](https://developer.clopos.com/)

## Main functionalities

- Library supports both sync and async requests.
- All of the function and classes has been documented.
- As all of the functions/variables/classes has been typed, type-hinting is active
- The flow of the requests has been explained in the documentation.

## Installing

<div class="termy">

```console
pip install integrify-clopos
```

</div>

## Usage

To use these requests you need to set these environmental variables:

| Variable Name          | Purpose                                            | Header equivalent | Default Value |
| :--------------------- | :------------------------------------------------- | ----------------- | :-----------: |
| `CLOPOS_CLIENT_ID`     | Client ID given by Clopos (used only for auth)     | `-`               |      `-`      |
| `CLOPOS_CLIENT_SECRET` | Client Secret given by Clopos (used only for auth) | `-`               |      `-`      |
| `CLOPOS_BRAND`         | Brand that you want to request                     | `x-brand`         |      `-`      |
| `CLOPOS_VENUE_ID`      | Venue/Branch id that you want to request           | `x-venue`         |      `-`      |

Note that, these values MIGHT be unset. In this case, you should send it in header of each request. Let's say you want to request menu categories of two venues separately:

```python
# CLOPOS_CLIENT_ID, CLOPOS_CLIENT_SECRET and CLOPOS_BRAND have been set as env variables
from integrify.clopos.client import CloposClient

venue1_id=1
venue2_id=2

token1 = CloposClient.auth(venue_id=venue1_id).body.token
categories1 = CloposClient.get_categories(headers={'x-token': token1, 'x-venue': venue1_id}).body.data

token2 = CloposClient.auth(venue_id=venue2_id).body.token
categories2 = CloposClient.get_categories(headers={'x-token': token1, 'x-venue': venue2_id}).body.data
```

If you want to fetch categories from different brand, just manually add `x-brand` to the header.

For auth, instead of headers, you will just send these as params.

```python
# No env was set
from integrify.clopos.client import CloposClient

client_id='eNUKI04aYJRU6TBhh5bwUrvmEORgQoxM'
client_secret='dqYkWUpDjzvKOgbP3ar8tSNKJbwMyYe1V5R7DHClfSNYkap5C5XxRA6PmzoPv1I2'
brand='openapitest'
venue_id='1'

token = CloposClient.auth(client_id=client_id, client_secret=client_secret, brand=brand, venue_id=venue_id).body.token
```

### List of requests

| Request function      | Purpose                     |         Clopos API          |
| :-------------------- | :-------------------------- | :-------------------------: |
| `auth`                | Authenticate, get token     |      `/open-api/auth`       |
| `get_venues`          | Get list of venues/branches |     `/open-api/venues`      |
| `get_users`           | Get list of users           |      `/open-api/users`      |
| `get_user_by_id`      | Get user by id              |   `/open-api/users/{id}`    |
| `get_customers`       | Get list of customers       |    `/open-api/customers`    |
| `get_customer_by_id`  | Get customer by id          | `/open-api/customers/{id}`  |
| `get_customer_groups` | Get list of customer groups | `/open-api/customer-group`  |
| `get_categories`      | Get list of menu categories |   `/open-api/categories`    |
| `get_category_by_id`  | Get menu category by id     | `/open-api/categories/{id}` |
| `get_stations`        | Get list of stations        |    `/open-api/stations`     |
| `get_station_by_id`   | Get station by id           |  `/open-api/stations/{id}`  |
| `get_products`        | Get list of products        |    `/open-api/products`     |
| `get_product_by_id`   | Get product by id           |  `/open-api/products/{id}`  |
| `get_sale_types`      | Get list of sale types      |   `/open-api/sale-types`    |
| `get_payment_methods` | Get list of payment methods | `/open-api/payment-methods` |
| `get_orders`          | Get list of orders          |     `/open-api/orders`      |
| `get_order_by_id`     | Get order by id             |   `/open-api/orders/{id}`   |
| `create_order`        | Create new order            |     `/open-api/orders`      |
| `get_receipts`        | Get list of receipts        |    `/open-api/receipts`     |
| `get_receipt_by_id`   | Get receipt by id           |  `/open-api/receipts/{id}`  |
| `create_receipt`      | Create a new receipt        |    `/open-api/receipts`     |
| `delete_receipt`      | Delete a receipt            |  `/open-api/receipts/{id}`  |

Note that, each request should have parameter `headers={'x-token': token}`. For example:

```python
# CLOPOS_CLIENT_ID, CLOPOS_CLIENT_SECRET, CLOPOS_BRAND and CLOPOS_VENUE_ID have been set as env variables

from integrify.clopos.client import CloposClient

token = CloposClient.auth().body.token
user = CloposClient.get_user_by_id(id=1, headers={'x-token': token}).body.data
```

> [!Caution]
> Integrify is unofficial library, even though it is based on official documentation.

## Other supported integrations

<!-- AUTO-UPDATE SECTION -->
| Servis                                                                              |                                                        Əsas sorğular                                                         |                                                        Bütün sorğular                                                        | Dokumentləşdirilmə                                                                                                           | Real mühitdə test                                                                                                            | Əsas developer                                    |
| ----------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| [EPoint](https://github.com/Integrify-SDK/integrify-epoint-python)                  |                                                              ✅                                                               | ![loading](https://raw.githubusercontent.com/Integrify-SDK/integrify-docs-python/main/docs/az/docs/assets/spinner-solid.svg) | [Tam](https://integrify.mmzeynalli.dev/integrations/epoint/about/)                                                           | ✅                                                                                                                            | [Miradil Zeynallı](https://github.com/mmzeynalli) |
| [KapitalBank](https://github.com/Integrify-SDK/integrify-kapitalbank-python)        |                                                              ✅                                                               |                                                              ✅                                                               | [Tam](https://integrify.mmzeynalli.dev/integrations/kapital/about/)                                                          | ✅                                                                                                                            | [Zaman Kazımov](https://github.com/kazimovzaman2) |
| [LSIM](https://github.com/Integrify-SDK/integrify-lsim-python)                      |                                                              ✅                                                               |                                                              ✅                                                               | [Tam](https://integrify.mmzeynalli.dev/integrations/lsim/about/)                                                             | ✅                                                                                                                            | [Miradil Zeynallı](https://github.com/mmzeynalli) |
| [Posta Guvercini](https://github.com/Integrify-SDK/integrify-postaguvercini-python) |                                                              ✅                                                               |                                                              ✅                                                               | [Tam](https://integrify.mmzeynalli.dev/integrations/posta-guvercini/about/)                                                  | ✅                                                                                                                            | [Zaman Kazımov](https://github.com/kazimovzaman2) |
| [Azericard](https://github.com/Integrify-SDK/integrify-azericard-python)            |                                                              ✅                                                               | ![loading](https://raw.githubusercontent.com/Integrify-SDK/integrify-docs-python/main/docs/az/docs/assets/spinner-solid.svg) | [Tam](https://integrify.mmzeynalli.dev/integrations/azericard/about)                                                         | ![loading](https://raw.githubusercontent.com/Integrify-SDK/integrify-docs-python/main/docs/az/docs/assets/spinner-solid.svg) | [Miradil Zeynallı](https://github.com/mmzeynalli) |
| [Payriff](https://github.com/Integrify-SDK/integrify-payriff-python)                | ![loading](https://raw.githubusercontent.com/Integrify-SDK/integrify-docs-python/main/docs/az/docs/assets/spinner-solid.svg) | ![loading](https://raw.githubusercontent.com/Integrify-SDK/integrify-docs-python/main/docs/az/docs/assets/spinner-solid.svg) | ![loading](https://raw.githubusercontent.com/Integrify-SDK/integrify-docs-python/main/docs/az/docs/assets/spinner-solid.svg) | ![loading](https://raw.githubusercontent.com/Integrify-SDK/integrify-docs-python/main/docs/az/docs/assets/spinner-solid.svg) | [Vahid Həsənzadə](https://github.com/vahidzhe)    |
