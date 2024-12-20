from fastapi import APIRouter

from database import get_sorted_domains_metrics

router = APIRouter()


@router.get("/metrics/")
def domains_metrics():
    sorted_domains = get_sorted_domains_metrics()
    if sorted_domains:
        top_domains_count = {domain: count for domain, count in sorted_domains}
        return top_domains_count
    return {"message": "No Data Found"}
