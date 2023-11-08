from __future__ import annotations
from django.db import models

# Create your models here.


class Order(models.Model):
    class Status(models.TextChoices):
        WAITING = "waiting", "주문 수락 대기중"
        ACCEPTED = "accepted", "주문 접수 완료"
        REJECTED = "rejected", "주문 거절"
        DELIVERY_COMPLETE = "delivery complete", "배달완료"

    status = models.CharField(
        max_length=32,
        choices=Status.choices,
        help_text="주문 상태 값",
        default=Status.WAITING,
    )


class DaliyReportManager(models.Manager):
    """

    Args:
        models (통계 쿼리): django manager와 QuerySet
    """

    def get_list_by_created_at(
        self, created_at__gte, created_at__lt
    ) -> list[DaliyReport]:
        return list(
            self.raw(
                raw_query="""
        SELETE 
            DATE_TRUNC('day', O.created_at) AS day,
            COUNT(*) AS total_cnt,
            SUM(O.total_price) as total_sales
        FROM 
            orders_order O
        WHERE
            O.created_at >= %s AND O.created_at < %s
        GROUP BY
            DATE_TRUNC('day', O.created_at)
        ;                    
        """,
                params=[created_at__gte, created_at__lt],
            )
        )


class DaliyReport(models.Model):
    """
    일별 통계
    """

    day = models.DateField(help_text="날짜", primary_key=True)
    total_sales = models.IntegerField(help_text="일 주문 총매출")
    total_cnt = models.IntegerField(help_text="일 주문 건수")

    objects: DaliyReportManager = DaliyReportManager()

    class Meta:
        managed: bool = False  # managed=False 옵션이 부여된 Model을 UnManaged Model 이라고 부름

    def __repr__(self) -> str:
        return f"{self.day.strftime('%Y-%m-%d')} : DailyReport(total_cnt:{self.total_cnt}) total_sales: {self.total_sales})"
