# Integrify Template

Bu reponu istifadə etməklə yeni inteqrasiyaları yaradıb, ekosistemə uyğun alt-kitabaxanalar yaratmaq asanlaşır.

Addımlar:

1. Sağ yuxarı küncdə "Use this template -> Create new repository"
2. Lokalınıza yükləyin
3. `python create_local_configs.py` skriptini run edin
4. integration_name qovluğunu işləyəciyniz inteqrasiyanın adına dəyişin
5. Ümumi axtarış verib, `{replace}` string-ini axtarın, və həmin yerləri dəyişin
6. `pre-commit` və `uv` istifadə edin
7. `uv sync` istifade etdikdən sonra, `make` kommandlarından istifadə edə bilərsiniz
