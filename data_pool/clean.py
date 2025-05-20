from typing import List, Dict


def _normalize_keys(data: List[Dict]) -> List[Dict]:
    normalized = []
    for item in data:
        normalized.append({
            str(k).strip().lower(): str(v).strip() if v is not None else ''
            for k, v in item.items()
        })
    return normalized


def _deduplicate(data: List[Dict]) -> List[Dict]:
    seen = set()
    result = []
    for item in data:
        key = tuple(sorted(item.items()))
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


def clean_data(data: List[Dict]) -> List[Dict]:
    """Normalize records and remove duplicates."""
    return _deduplicate(_normalize_keys(data))
