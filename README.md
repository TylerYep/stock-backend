# stock-backend

Django App

```fish
python manage.py runserver 8989
```

```python
from guess.models import *
Stock.objects.filter(id="06a09f2d-8bb2-4f99-bdba-b800235e0ef5").explain(verbose=True)
Stock.objects.create(symbol="TSLA", price=Decimal("852.23"))
```