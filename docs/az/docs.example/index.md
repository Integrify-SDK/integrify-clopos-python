<p align="center">
  <a href="https://integrify.mmzeynalli.dev/"><img width="400" src="https://raw.githubusercontent.com/Integrify-SDK/integrify-{replace}-python/main/docs/az/docs/assets/integrify.png" alt="Integrify"></a>
</p>
<p align="center">
    <em>Integrify API inteqrasiyalarını rahatlaşdıran sorğular kitabaxanasıdır.</em>
</p>
<p  style='display:flex;flex-wrap:wrap;gap:5px;width:70%;justify-content:flex-start;margin: 0 auto;'>
<a href="https://github.com/Integrify-SDK/integrify-{replace}-python/actions/workflows/test.yml" target="_blank">
    <img src="https://github.com/Integrify-SDK/integrify-{replace}-python/actions/workflows/test.yml/badge.svg?branch=main" alt="Test">
</a>
<a href="https://github.com/Integrify-SDK/integrify-{replace}-python/actions/workflows/publish.yml" target="_blank">
    <img src="https://github.com/Integrify-SDK/integrify-{replace}-python/actions/workflows/publish.yml/badge.svg" alt="Publish">
</a>
<a href="https://pypi.org/project/integrify" target="_blank">
  <img src="https://img.shields.io/pypi/v/integrify?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://app.netlify.com/sites/integrify-docs/deploys">
  <img src="https://api.netlify.com/api/v1/badges/d8931b6a-80c7-41cb-bdbb-bf6ef5789f80/deploy-status" alt="Netlify Status">
</a>
<a href="https://pepy.tech/project/integrify" target="_blank">
  <img src="https://static.pepy.tech/badge/integrify" alt="Downloads">
</a>
<a href="https://pypi.org/project/integrify" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/integrify.svg?color=%2334D058" alt="Supported Python versions">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/Integrify-SDK/integrify-{replace}-python" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/Integrify-SDK/integrify-{replace}-python.svg" alt="Coverage">
</a>

</p>

---

**Dokumentasiya**: [https://integrify.mmzeynalli.dev](https://integrify.mmzeynalli.dev)

**Kod**: [https://github.com/Integrify-SDK/integrify-{replace}-python](https://github.com/Integrify-SDK/integrify-{replace}-python)

---

## Əsas özəlliklər { #main-features }

- Kitabxana həm sync, həm də async sorğu dəyişimini dəstəkləyir.
- Kitabaxanadakı bütün sinif və funksiyalar tamamilə dokumentləşdirilib.
- Kitabaxanadakı bütün sinif və funksiyalar tipləndirildiyindən, "type hinting" aktivdir.
- Sorğuların çoxunun məntiq axını (flowsu) izah edilib.

---

## Kitabxananın yüklənməsi { #installation }

<div class="termy">

```console
$ pip install {replace}
```

</div>

## İstifadəsi { #usage }

{replace} üçün sorğuları istifadə etmək istərsək:

### Sync

```python
from integrify.{replace} import {replace}

resp = {replace}
print(resp.ok, resp.body)

```

### Async

```python
from integrify.{replace} import {replace}

# Async main loop artıq başlamışdır
resp = await {replace}
print(resp.ok, resp.body)

```

### Sorğu cavabı { #request-response }

Yuxarıdakı sorğuların (və ya istənilən sorğunun) cavab formatı `ApiResponse` class-ıdır:

```python
class ApiResponse:
    ok: bool
    """Cavab sorğusunun statusu 400dən kiçikdirsə"""

    status_code: int
    """Cavab sorğusunun status kodu"""

    headers: dict
    """Cavab sorğusunun header-i"""

    body: Dəyişkən
    """Cavab sorğusunun body-si"""
```

## Dəstəklənən başqa API inteqrasiyaları

???+ warning
    Bütün sorğular rəsmi dokumentasiyalara uyğun yazılsalar da, Integrify qeyri-rəsmi API klient-dir.

<!-- AUTO-UPDATE SECTION -->