CREATE TABLE AS SELECT : SELECT 문장을 이용하여 다른 테이블이 있는 데이터를 복사하여 새로운 테이블을 생성

```sql
CREATE TABLE TEST_TABLE_THREE 
         AS SELECT IDX,ID,NAME,AMT FROM TEST_TABLE_ONE;

```

inline view (더 다중으로도 가능함)

```sql
SELECT A.*
	FORM
(
	SELECT
    		NAME
    		,CREDIT
    		FROM CUSTROMERS

)A;
```

CREATE OR REPLACE VIEW (긴 코드에 대한 함수 같은 것 설정)

```sql
CREATE OR REPLACE VIEW CUSTOMER_SALES AS ~

SELECT * FROM CUSTOMER_SALES;
```

서브 쿼리(기본) where 안에 select

![image-20220507022202639](sql%20%EC%A0%95%EB%A6%AC.assets/image-20220507022202639.png)

서브 쿼리 (스칼라) select 안에 select

![image-20220507022624633](sql%20%EC%A0%95%EB%A6%AC.assets/image-20220507022624633.png)

인라인 뷰 서브 쿼리 from 안에 select

![image-20220507023446498](sql%20%EC%A0%95%EB%A6%AC.assets/image-20220507023446498.png)
