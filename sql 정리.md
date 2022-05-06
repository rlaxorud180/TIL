CREATE TABLE AS SELECT : SELECT 문장을 이용하여 다른 테이블이 있는 데이터를 복사하여 새로운 테이블을 생성

```sql
CREATE TABLE TEST_TABLE_THREE 
         AS SELECT IDX,ID,NAME,AMT FROM TEST_TABLE_ONE;

```

