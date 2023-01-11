>>> empDf = spark.read.option("header",True).option("inferSchema",True).csv("/input_data/employees.csv")
>>> empDf.show()
+-----------+----------+---------+--------+------------+---------+----------+------+--------------+----------+-------------+
|EMPLOYEE_ID|FIRST_NAME|LAST_NAME|   EMAIL|PHONE_NUMBER|HIRE_DATE|    JOB_ID|SALARY|COMMISSION_PCT|MANAGER_ID|DEPARTMENT_ID|
+-----------+----------+---------+--------+------------+---------+----------+------+--------------+----------+-------------+
|        198|    Donald| OConnell|DOCONNEL|650.507.9833|21-JUN-07|  SH_CLERK|  2600|            - |       124|           50|
|        199|   Douglas|    Grant|  DGRANT|650.507.9844|13-JAN-08|  SH_CLERK|  2600|            - |       124|           50|
|        200|  Jennifer|   Whalen| JWHALEN|515.123.4444|17-SEP-03|   AD_ASST|  4400|            - |       101|           10|
|        201|   Michael|Hartstein|MHARTSTE|515.123.5555|17-FEB-04|    MK_MAN| 13000|            - |       100|           20|
|        202|       Pat|      Fay|    PFAY|603.123.6666|17-AUG-05|    MK_REP|  6000|            - |       201|           20|
|        203|     Susan|   Mavris| SMAVRIS|515.123.7777|07-JUN-02|    HR_REP|  6500|            - |       101|           40|
|        204|   Hermann|     Baer|   HBAER|515.123.8888|07-JUN-02|    PR_REP| 10000|            - |       101|           70|
|        205|   Shelley|  Higgins|SHIGGINS|515.123.8080|07-JUN-02|    AC_MGR| 12008|            - |       101|          110|
|        206|   William|    Gietz|  WGIETZ|515.123.8181|07-JUN-02|AC_ACCOUNT|  8300|            - |       205|          110|
|        100|    Steven|     King|   SKING|515.123.4567|17-JUN-03|   AD_PRES| 24000|            - |        - |           90|
|        101|     Neena|  Kochhar|NKOCHHAR|515.123.4568|21-SEP-05|     AD_VP| 17000|            - |       100|           90|
|        102|       Lex|  De Haan| LDEHAAN|515.123.4569|13-JAN-01|     AD_VP| 17000|            - |       100|           90|
|        103| Alexander|   Hunold| AHUNOLD|590.423.4567|03-JAN-06|   IT_PROG|  9000|            - |       102|           60|
|        104|     Bruce|    Ernst|  BERNST|590.423.4568|21-MAY-07|   IT_PROG|  6000|            - |       103|           60|
|        105|     David|   Austin| DAUSTIN|590.423.4569|25-JUN-05|   IT_PROG|  4800|            - |       103|           60|
|        106|     Valli|Pataballa|VPATABAL|590.423.4560|05-FEB-06|   IT_PROG|  4800|            - |       103|           60|
|        107|     Diana|  Lorentz|DLORENTZ|590.423.5567|07-FEB-07|   IT_PROG|  4200|            - |       103|           60|
|        108|     Nancy|Greenberg|NGREENBE|515.124.4569|17-AUG-02|    FI_MGR| 12008|            - |       101|          100|
|        109|    Daniel|   Faviet| DFAVIET|515.124.4169|16-AUG-02|FI_ACCOUNT|  9000|            - |       108|          100|
|        110|      John|     Chen|   JCHEN|515.124.4269|28-SEP-05|FI_ACCOUNT|  8200|            - |       108|          100|
+-----------+----------+---------+--------+------------+---------+----------+------+--------------+----------+-------------+
only showing top 20 rows


>>> from pyspark.sql.functions import *
>>> empDf.count()
50
>>> empDf.select(count("salary")).show()
+-------------+
|count(salary)|
+-------------+
|           50|
+-------------+


>>> empDf.select(count("salary")).alias("total_count").show()
+-------------+
|count(salary)|
+-------------+
|           50|
+-------------+

>>> empDf.select(count("salary").alias("total_count")).show()
+-----------+
|total_count|
+-----------+
|         50|
+-----------+

>>> empDf.select(max("salary").alias("max_salary")).show()
+----------+
|max_salary|
+----------+
|     24000|
+----------+

>>> empDf.select(min("salary").alias("min_salary")).show()
+----------+
|min_salary|
+----------+
|      2100|
+----------+

>>> empDf.select(avg("salary").alias("avg_salary")).show()
+----------+
|avg_salary|
+----------+
|   6182.32|
+----------+

>>> empDf.select(sum("salary").alias("sum_salary")).show()
+----------+
|sum_salary|
+----------+
|    309116|
+----------+


>>> empDf.select("EMPLOYEE_ID",sum("salary").alias("sum_salary")).show()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/spark/python/pyspark/sql/dataframe.py", line 1685, in select
    jdf = self._jdf.select(self._jcols(*cols))
  File "/usr/local/spark/python/lib/py4j-0.10.9.3-src.zip/py4j/java_gateway.py", line 1321, in __call__
  File "/usr/local/spark/python/pyspark/sql/utils.py", line 117, in deco
    raise converted from None
pyspark.sql.utils.AnalysisException: grouping expressions sequence is empty, and 'EMPLOYEE_ID' is not an aggregate function. Wrap '(sum(salary) AS sum_salary)' in windowing function(s) or wrap 'EMPLOYEE_ID' in first() (or first_value) if you don't care which value you get.;
Aggregate [EMPLOYEE_ID#16, sum(salary#23) AS sum_salary#206L]
+- Relation [EMPLOYEE_ID#16,FIRST_NAME#17,LAST_NAME#18,EMAIL#19,PHONE_NUMBER#20,HIRE_DATE#21,JOB_ID#22,SALARY#23,COMMISSION_PCT#24,MANAGER_ID#25,DEPARTMENT_ID#26] csv


>>> empDf.select("EMPLOYEE_ID","FIRST_NAME","DEPARTMENT_ID","SALARY").orderBy("salary").show()
+-----------+----------+-------------+------+
|EMPLOYEE_ID|FIRST_NAME|DEPARTMENT_ID|SALARY|
+-----------+----------+-------------+------+
|        132|        TJ|           50|  2100|
|        136|     Hazel|           50|  2200|
|        128|    Steven|           50|  2200|
|        127|     James|           50|  2400|
|        135|        Ki|           50|  2400|
|        131|     James|           50|  2500|
|        119|     Karen|           30|  2500|
|        140|    Joshua|           50|  2500|
|        198|    Donald|           50|  2600|
|        199|   Douglas|           50|  2600|
|        118|       Guy|           30|  2600|
|        126|     Irene|           50|  2700|
|        139|      John|           50|  2700|
|        130|     Mozhe|           50|  2800|
|        117|     Sigal|           30|  2800|
|        116|    Shelli|           30|  2900|
|        134|   Michael|           50|  2900|
|        115| Alexander|           30|  3100|
|        125|     Julia|           50|  3200|
|        138|   Stephen|           50|  3200|
+-----------+----------+-------------+------+
only showing top 20 rows


>>> empDf.select("EMPLOYEE_ID","FIRST_NAME","DEPARTMENT_ID","SALARY").orderBy(col("DEPARTMENT_ID").asc(),col("SALARY").desc()).show()
+-----------+----------+-------------+------+
|EMPLOYEE_ID|FIRST_NAME|DEPARTMENT_ID|SALARY|
+-----------+----------+-------------+------+
|        200|  Jennifer|           10|  4400|
|        201|   Michael|           20| 13000|
|        202|       Pat|           20|  6000|
|        114|       Den|           30| 11000|
|        115| Alexander|           30|  3100|
|        116|    Shelli|           30|  2900|
|        117|     Sigal|           30|  2800|
|        118|       Guy|           30|  2600|
|        119|     Karen|           30|  2500|
|        203|     Susan|           40|  6500|
|        121|      Adam|           50|  8200|
|        120|   Matthew|           50|  8000|
|        122|     Payam|           50|  7900|
|        123|    Shanta|           50|  6500|
|        124|     Kevin|           50|  5800|
|        137|    Renske|           50|  3600|
|        133|     Jason|           50|  3300|
|        129|     Laura|           50|  3300|
|        125|     Julia|           50|  3200|
|        138|   Stephen|           50|  3200|
+-----------+----------+-------------+------+
only showing top 20 rows


>>> empDf.groupBy("DEPARTMENT_ID").sum("SALARY").show(100)
+-------------+-----------+
|DEPARTMENT_ID|sum(SALARY)|
+-------------+-----------+
|           20|      19000|
|           40|       6500|
|          100|      51608|
|           10|       4400|
|           50|      85600|
|           70|      10000|
|           90|      58000|
|           60|      28800|
|          110|      20308|
|           30|      24900|
+-------------+-----------+


>>> empDf.groupBy("DEPARTMENT_ID","JOB_ID").sum("SALARY").show(100)
+-------------+----------+-----------+
|DEPARTMENT_ID|    JOB_ID|sum(SALARY)|
+-------------+----------+-----------+
|           90|   AD_PRES|      24000|
|           30|    PU_MAN|      11000|
|           70|    PR_REP|      10000|
|           50|    ST_MAN|      36400|
|           40|    HR_REP|       6500|
|           60|   IT_PROG|      28800|
|           10|   AD_ASST|       4400|
|           30|  PU_CLERK|      13900|
|           50|  ST_CLERK|      44000|
|           20|    MK_REP|       6000|
|           50|  SH_CLERK|       5200|
|           90|     AD_VP|      34000|
|          100|FI_ACCOUNT|      39600|
|          110|    AC_MGR|      12008|
|          110|AC_ACCOUNT|       8300|
|           20|    MK_MAN|      13000|
|          100|    FI_MGR|      12008|
+-------------+----------+-----------+


>>> empDf.groupBy("DEPARTMENT_ID","JOB_ID").sum("SALARY","EMPLOYEE_ID").show(100)
+-------------+----------+-----------+----------------+
|DEPARTMENT_ID|    JOB_ID|sum(SALARY)|sum(EMPLOYEE_ID)|
+-------------+----------+-----------+----------------+
|           90|   AD_PRES|      24000|             100|
|           30|    PU_MAN|      11000|             114|
|           70|    PR_REP|      10000|             204|
|           50|    ST_MAN|      36400|             610|
|           40|    HR_REP|       6500|             203|
|           60|   IT_PROG|      28800|             525|
|           10|   AD_ASST|       4400|             200|
|           30|  PU_CLERK|      13900|             585|
|           50|  ST_CLERK|      44000|            2120|
|           20|    MK_REP|       6000|             202|
|           50|  SH_CLERK|       5200|             397|
|           90|     AD_VP|      34000|             203|
|          100|FI_ACCOUNT|      39600|             555|
|          110|    AC_MGR|      12008|             205|
|          110|AC_ACCOUNT|       8300|             206|
|           20|    MK_MAN|      13000|             201|
|          100|    FI_MGR|      12008|             108|
+-------------+----------+-----------+----------------+


>>> empDf.groupBy("DEPARTMENT_ID").agg(sum("SALARY").alias("SUM_SALARY"),max("SALARY").alias("MAX_SALARY"),min("SALARY").alias("MIN_SALARY"),avg("SALARY").alias("AVG_SALARY")).show()
+-------------+----------+----------+----------+------------------+
|DEPARTMENT_ID|SUM_SALARY|MAX_SALARY|MIN_SALARY|        AVG_SALARY|
+-------------+----------+----------+----------+------------------+
|           20|     19000|     13000|      6000|            9500.0|
|           40|      6500|      6500|      6500|            6500.0|
|          100|     51608|     12008|      6900| 8601.333333333334|
|           10|      4400|      4400|      4400|            4400.0|
|           50|     85600|      8200|      2100|3721.7391304347825|
|           70|     10000|     10000|     10000|           10000.0|
|           90|     58000|     24000|     17000|19333.333333333332|
|           60|     28800|      9000|      4200|            5760.0|
|          110|     20308|     12008|      8300|           10154.0|
|           30|     24900|     11000|      2500|            4150.0|
+-------------+----------+----------+----------+------------------+


>>> empDf.groupBy("DEPARTMENT_ID").agg(sum("SALARY").alias("SUM_SALARY"),max("SALARY").alias("MAX_SALARY"),min("SALARY").alias("MIN_SALARY"),avg("SALARY").alias("AVG_SALARY")).where(col("MAX_SALARY") >= 10000).show()
+-------------+----------+----------+----------+------------------+
|DEPARTMENT_ID|SUM_SALARY|MAX_SALARY|MIN_SALARY|        AVG_SALARY|
+-------------+----------+----------+----------+------------------+
|           20|     19000|     13000|      6000|            9500.0|
|          100|     51608|     12008|      6900| 8601.333333333334|
|           70|     10000|     10000|     10000|           10000.0|
|           90|     58000|     24000|     17000|19333.333333333332|
|          110|     20308|     12008|      8300|           10154.0|
|           30|     24900|     11000|      2500|            4150.0|
+-------------+----------+----------+----------+------------------+


>>> df = empDf.withColumn("EMP_GRADE",when(col("SALARY") > 15000,"A").when( (col("SALARY") >= 10000) & ( col("SALARY") < 15000),"B").otherwise("C"))
>>> df.select("EMPLOYEE_ID","SALARY","EMP_GRADE").show()
+-----------+------+---------+
|EMPLOYEE_ID|SALARY|EMP_GRADE|
+-----------+------+---------+
|        198|  2600|        C|
|        199|  2600|        C|
|        200|  4400|        C|
|        201| 13000|        B|
|        202|  6000|        C|
|        203|  6500|        C|
|        204| 10000|        B|
|        205| 12008|        B|
|        206|  8300|        C|
|        100| 24000|        A|
|        101| 17000|        A|
|        102| 17000|        A|
|        103|  9000|        C|
|        104|  6000|        C|
|        105|  4800|        C|
|        106|  4800|        C|
|        107|  4200|        C|
|        108| 12008|        B|
|        109|  9000|        C|
|        110|  8200|        C|
+-----------+------+---------+
only showing top 20 rows


>>> empDf.createOrReplaceTempView("employee")
>>> spark.sql("select * from employee limit 5").show()
+-----------+----------+---------+--------+------------+---------+--------+------+--------------+----------+-------------+
|EMPLOYEE_ID|FIRST_NAME|LAST_NAME|   EMAIL|PHONE_NUMBER|HIRE_DATE|  JOB_ID|SALARY|COMMISSION_PCT|MANAGER_ID|DEPARTMENT_ID|
+-----------+----------+---------+--------+------------+---------+--------+------+--------------+----------+-------------+
|        198|    Donald| OConnell|DOCONNEL|650.507.9833|21-JUN-07|SH_CLERK|  2600|            - |       124|           50|
|        199|   Douglas|    Grant|  DGRANT|650.507.9844|13-JAN-08|SH_CLERK|  2600|            - |       124|           50|
|        200|  Jennifer|   Whalen| JWHALEN|515.123.4444|17-SEP-03| AD_ASST|  4400|            - |       101|           10|
|        201|   Michael|Hartstein|MHARTSTE|515.123.5555|17-FEB-04|  MK_MAN| 13000|            - |       100|           20|
|        202|       Pat|      Fay|    PFAY|603.123.6666|17-AUG-05|  MK_REP|  6000|            - |       201|           20|
+-----------+----------+---------+--------+------------+---------+--------+------+--------------+----------+-------------+


>>> df = spark.sql("select employee_id,salary from employee")
>>> df.show(100)
+-----------+------+
|employee_id|salary|
+-----------+------+
|        198|  2600|
|        199|  2600|
|        200|  4400|
|        201| 13000|
|        202|  6000|
|        203|  6500|
|        204| 10000|
|        205| 12008|
|        206|  8300|
|        100| 24000|
|        101| 17000|
|        102| 17000|
|        103|  9000|
|        104|  6000|
|        105|  4800|
|        106|  4800|
|        107|  4200|
|        108| 12008|
|        109|  9000|
|        110|  8200|
|        111|  7700|
|        112|  7800|
|        113|  6900|
|        114| 11000|
|        115|  3100|
|        116|  2900|
|        117|  2800|
|        118|  2600|
|        119|  2500|
|        120|  8000|
|        121|  8200|
|        122|  7900|
|        123|  6500|
|        124|  5800|
|        125|  3200|
|        126|  2700|
|        127|  2400|
|        128|  2200|
|        129|  3300|
|        130|  2800|
|        131|  2500|
|        132|  2100|
|        133|  3300|
|        134|  2900|
|        135|  2400|
|        136|  2200|
|        137|  3600|
|        138|  3200|
|        139|  2700|
|        140|  2500|
+-----------+------+



>>> spark.sql("select department_id,sum(salary) as sum_salary from employee group by department_id").show()
+-------------+----------+
|department_id|sum_salary|
+-------------+----------+
|           20|     19000|
|           40|      6500|
|          100|     51608|
|           10|      4400|
|           50|     85600|
|           70|     10000|
|           90|     58000|
|           60|     28800|
|          110|     20308|
|           30|     24900|
+-------------+----------+



>>> spark.sql("select employee_id,department_id,rank() over(partition by department_id order by salary desc) as rank_salary from employee").show()
+-----------+-------------+-----------+
|employee_id|department_id|rank_salary|
+-----------+-------------+-----------+
|        200|           10|          1|
|        201|           20|          1|
|        202|           20|          2|
|        114|           30|          1|
|        115|           30|          2|
|        116|           30|          3|
|        117|           30|          4|
|        118|           30|          5|
|        119|           30|          6|
|        203|           40|          1|
|        121|           50|          1|
|        120|           50|          2|
|        122|           50|          3|
|        123|           50|          4|
|        124|           50|          5|
|        137|           50|          6|
|        129|           50|          7|
|        133|           50|          7|
|        125|           50|          9|
|        138|           50|          9|
+-----------+-------------+-----------+
only showing top 20 rows


>>> deptDf = spark.read.option("header",True).option("inferSchema",True).csv("/input_data/departments.csv")
>>> deptDf.show()
+-------------+--------------------+----------+-----------+
|DEPARTMENT_ID|     DEPARTMENT_NAME|MANAGER_ID|LOCATION_ID|
+-------------+--------------------+----------+-----------+
|           10|      Administration|       200|       1700|
|           20|           Marketing|       201|       1800|
|           30|          Purchasing|       114|       1700|
|           40|     Human Resources|       203|       2400|
|           50|            Shipping|       121|       1500|
|           60|                  IT|       103|       1400|
|           70|    Public Relations|       204|       2700|
|           80|               Sales|       145|       2500|
|           90|           Executive|       100|       1700|
|          100|             Finance|       108|       1700|
|          110|          Accounting|       205|       1700|
|          120|            Treasury|        - |       1700|
|          130|       Corporate Tax|        - |       1700|
|          140|  Control And Credit|        - |       1700|
|          150|Shareholder Services|        - |       1700|
|          160|            Benefits|        - |       1700|
|          170|       Manufacturing|        - |       1700|
|          180|        Construction|        - |       1700|
|          190|         Contracting|        - |       1700|
|          200|          Operations|        - |       1700|
+-------------+--------------------+----------+-----------+
only showing top 20 rows


>>> empDf.join(deptDf, empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "inner").show()
+-----------+----------+---------+--------+------------+---------+----------+------+--------------+----------+-------------+-------------+----------------+----------+-----------+
|EMPLOYEE_ID|FIRST_NAME|LAST_NAME|   EMAIL|PHONE_NUMBER|HIRE_DATE|    JOB_ID|SALARY|COMMISSION_PCT|MANAGER_ID|DEPARTMENT_ID|DEPARTMENT_ID| DEPARTMENT_NAME|MANAGER_ID|LOCATION_ID|
+-----------+----------+---------+--------+------------+---------+----------+------+--------------+----------+-------------+-------------+----------------+----------+-----------+
|        198|    Donald| OConnell|DOCONNEL|650.507.9833|21-JUN-07|  SH_CLERK|  2600|            - |       124|           50|           50|        Shipping|       121|       1500|
|        199|   Douglas|    Grant|  DGRANT|650.507.9844|13-JAN-08|  SH_CLERK|  2600|            - |       124|           50|           50|        Shipping|       121|       1500|
|        200|  Jennifer|   Whalen| JWHALEN|515.123.4444|17-SEP-03|   AD_ASST|  4400|            - |       101|           10|           10|  Administration|       200|       1700|
|        201|   Michael|Hartstein|MHARTSTE|515.123.5555|17-FEB-04|    MK_MAN| 13000|            - |       100|           20|           20|       Marketing|       201|       1800|
|        202|       Pat|      Fay|    PFAY|603.123.6666|17-AUG-05|    MK_REP|  6000|            - |       201|           20|           20|       Marketing|       201|       1800|
|        203|     Susan|   Mavris| SMAVRIS|515.123.7777|07-JUN-02|    HR_REP|  6500|            - |       101|           40|           40| Human Resources|       203|       2400|
|        204|   Hermann|     Baer|   HBAER|515.123.8888|07-JUN-02|    PR_REP| 10000|            - |       101|           70|           70|Public Relations|       204|       2700|
|        205|   Shelley|  Higgins|SHIGGINS|515.123.8080|07-JUN-02|    AC_MGR| 12008|            - |       101|          110|          110|      Accounting|       205|       1700|
|        206|   William|    Gietz|  WGIETZ|515.123.8181|07-JUN-02|AC_ACCOUNT|  8300|            - |       205|          110|          110|      Accounting|       205|       1700|
|        100|    Steven|     King|   SKING|515.123.4567|17-JUN-03|   AD_PRES| 24000|            - |        - |           90|           90|       Executive|       100|       1700|
|        101|     Neena|  Kochhar|NKOCHHAR|515.123.4568|21-SEP-05|     AD_VP| 17000|            - |       100|           90|           90|       Executive|       100|       1700|
|        102|       Lex|  De Haan| LDEHAAN|515.123.4569|13-JAN-01|     AD_VP| 17000|            - |       100|           90|           90|       Executive|       100|       1700|
|        103| Alexander|   Hunold| AHUNOLD|590.423.4567|03-JAN-06|   IT_PROG|  9000|            - |       102|           60|           60|              IT|       103|       1400|
|        104|     Bruce|    Ernst|  BERNST|590.423.4568|21-MAY-07|   IT_PROG|  6000|            - |       103|           60|           60|              IT|       103|       1400|
|        105|     David|   Austin| DAUSTIN|590.423.4569|25-JUN-05|   IT_PROG|  4800|            - |       103|           60|           60|              IT|       103|       1400|
|        106|     Valli|Pataballa|VPATABAL|590.423.4560|05-FEB-06|   IT_PROG|  4800|            - |       103|           60|           60|              IT|       103|       1400|
|        107|     Diana|  Lorentz|DLORENTZ|590.423.5567|07-FEB-07|   IT_PROG|  4200|            - |       103|           60|           60|              IT|       103|       1400|
|        108|     Nancy|Greenberg|NGREENBE|515.124.4569|17-AUG-02|    FI_MGR| 12008|            - |       101|          100|          100|         Finance|       108|       1700|
|        109|    Daniel|   Faviet| DFAVIET|515.124.4169|16-AUG-02|FI_ACCOUNT|  9000|            - |       108|          100|          100|         Finance|       108|       1700|
|        110|      John|     Chen|   JCHEN|515.124.4269|28-SEP-05|FI_ACCOUNT|  8200|            - |       108|          100|          100|         Finance|       108|       1700|
+-----------+----------+---------+--------+------------+---------+----------+------+--------------+----------+-------------+-------------+----------------+----------+-----------+
only showing top 20 rows


>>> empDf.join(deptDf, empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "inner").select(empDf.EMPLOYEE_ID, empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME).show()
+-----------+-------------+---------------+
|EMPLOYEE_ID|DEPARTMENT_ID|DEPARTMENT_NAME|
+-----------+-------------+---------------+
|        200|           10| Administration|
|        202|           20|      Marketing|
|        201|           20|      Marketing|
|        119|           30|     Purchasing|
|        118|           30|     Purchasing|
|        117|           30|     Purchasing|
|        116|           30|     Purchasing|
|        115|           30|     Purchasing|
|        114|           30|     Purchasing|
|        203|           40|Human Resources|
|        140|           50|       Shipping|
|        139|           50|       Shipping|
|        138|           50|       Shipping|
|        137|           50|       Shipping|
|        136|           50|       Shipping|
|        135|           50|       Shipping|
|        134|           50|       Shipping|
|        133|           50|       Shipping|
|        132|           50|       Shipping|
|        131|           50|       Shipping|
+-----------+-------------+---------------+
only showing top 20 rows


>>> empDf.join(deptDf, empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "left").select(empDf.EMPLOYEE_ID, empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME).show(100)
+-----------+-------------+----------------+
|EMPLOYEE_ID|DEPARTMENT_ID| DEPARTMENT_NAME|
+-----------+-------------+----------------+
|        198|           50|        Shipping|
|        199|           50|        Shipping|
|        200|           10|  Administration|
|        201|           20|       Marketing|
|        202|           20|       Marketing|
|        203|           40| Human Resources|
|        204|           70|Public Relations|
|        205|          110|      Accounting|
|        206|          110|      Accounting|
|        100|           90|       Executive|
|        101|           90|       Executive|
|        102|           90|       Executive|
|        103|           60|              IT|
|        104|           60|              IT|
|        105|           60|              IT|
|        106|           60|              IT|
|        107|           60|              IT|
|        108|          100|         Finance|
|        109|          100|         Finance|
|        110|          100|         Finance|
|        111|          100|         Finance|
|        112|          100|         Finance|
|        113|          100|         Finance|
|        114|           30|      Purchasing|
|        115|           30|      Purchasing|
|        116|           30|      Purchasing|
|        117|           30|      Purchasing|
|        118|           30|      Purchasing|
|        119|           30|      Purchasing|
|        120|           50|        Shipping|
|        121|           50|        Shipping|
|        122|           50|        Shipping|
|        123|           50|        Shipping|
|        124|           50|        Shipping|
|        125|           50|        Shipping|
|        126|           50|        Shipping|
|        127|           50|        Shipping|
|        128|           50|        Shipping|
|        129|           50|        Shipping|
|        130|           50|        Shipping|
|        131|           50|        Shipping|
|        132|           50|        Shipping|
|        133|           50|        Shipping|
|        134|           50|        Shipping|
|        135|           50|        Shipping|
|        136|           50|        Shipping|
|        137|           50|        Shipping|
|        138|           50|        Shipping|
|        139|           50|        Shipping|
|        140|           50|        Shipping|
+-----------+-------------+----------------+


>>> empDf.join(deptDf, empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "right").select(empDf.EMPLOYEE_ID, empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME).show(100)
+-----------+-------------+--------------------+
|EMPLOYEE_ID|DEPARTMENT_ID|     DEPARTMENT_NAME|
+-----------+-------------+--------------------+
|        200|           10|      Administration|
|        202|           20|           Marketing|
|        201|           20|           Marketing|
|        119|           30|          Purchasing|
|        118|           30|          Purchasing|
|        117|           30|          Purchasing|
|        116|           30|          Purchasing|
|        115|           30|          Purchasing|
|        114|           30|          Purchasing|
|        203|           40|     Human Resources|
|        140|           50|            Shipping|
|        139|           50|            Shipping|
|        138|           50|            Shipping|
|        137|           50|            Shipping|
|        136|           50|            Shipping|
|        135|           50|            Shipping|
|        134|           50|            Shipping|
|        133|           50|            Shipping|
|        132|           50|            Shipping|
|        131|           50|            Shipping|
|        130|           50|            Shipping|
|        129|           50|            Shipping|
|        128|           50|            Shipping|
|        127|           50|            Shipping|
|        126|           50|            Shipping|
|        125|           50|            Shipping|
|        124|           50|            Shipping|
|        123|           50|            Shipping|
|        122|           50|            Shipping|
|        121|           50|            Shipping|
|        120|           50|            Shipping|
|        199|           50|            Shipping|
|        198|           50|            Shipping|
|        107|           60|                  IT|
|        106|           60|                  IT|
|        105|           60|                  IT|
|        104|           60|                  IT|
|        103|           60|                  IT|
|        204|           70|    Public Relations|
|       null|         null|               Sales|
|        102|           90|           Executive|
|        101|           90|           Executive|
|        100|           90|           Executive|
|        113|          100|             Finance|
|        112|          100|             Finance|
|        111|          100|             Finance|
|        110|          100|             Finance|
|        109|          100|             Finance|
|        108|          100|             Finance|
|        206|          110|          Accounting|
|        205|          110|          Accounting|
|       null|         null|            Treasury|
|       null|         null|       Corporate Tax|
|       null|         null|  Control And Credit|
|       null|         null|Shareholder Services|
|       null|         null|            Benefits|
|       null|         null|       Manufacturing|
|       null|         null|        Construction|
|       null|         null|         Contracting|
|       null|         null|          Operations|
|       null|         null|          IT Support|
|       null|         null|                 NOC|
|       null|         null|         IT Helpdesk|
|       null|         null|    Government Sales|
|       null|         null|        Retail Sales|
|       null|         null|          Recruiting|
|       null|         null|             Payroll|
+-----------+-------------+--------------------+



>>> empDf.join(deptDf, empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "fullouter").select(empDf.EMPLOYEE_ID, empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME).show(100)
+-----------+-------------+--------------------+
|EMPLOYEE_ID|DEPARTMENT_ID|     DEPARTMENT_NAME|
+-----------+-------------+--------------------+
|        200|           10|      Administration|
|        201|           20|           Marketing|
|        202|           20|           Marketing|
|        114|           30|          Purchasing|
|        115|           30|          Purchasing|
|        116|           30|          Purchasing|
|        117|           30|          Purchasing|
|        118|           30|          Purchasing|
|        119|           30|          Purchasing|
|        203|           40|     Human Resources|
|        198|           50|            Shipping|
|        199|           50|            Shipping|
|        120|           50|            Shipping|
|        121|           50|            Shipping|
|        122|           50|            Shipping|
|        123|           50|            Shipping|
|        124|           50|            Shipping|
|        125|           50|            Shipping|
|        126|           50|            Shipping|
|        127|           50|            Shipping|
|        128|           50|            Shipping|
|        129|           50|            Shipping|
|        130|           50|            Shipping|
|        131|           50|            Shipping|
|        132|           50|            Shipping|
|        133|           50|            Shipping|
|        134|           50|            Shipping|
|        135|           50|            Shipping|
|        136|           50|            Shipping|
|        137|           50|            Shipping|
|        138|           50|            Shipping|
|        139|           50|            Shipping|
|        140|           50|            Shipping|
|        103|           60|                  IT|
|        104|           60|                  IT|
|        105|           60|                  IT|
|        106|           60|                  IT|
|        107|           60|                  IT|
|        204|           70|    Public Relations|
|       null|         null|               Sales|
|        100|           90|           Executive|
|        101|           90|           Executive|
|        102|           90|           Executive|
|        108|          100|             Finance|
|        109|          100|             Finance|
|        110|          100|             Finance|
|        111|          100|             Finance|
|        112|          100|             Finance|
|        113|          100|             Finance|
|        205|          110|          Accounting|
|        206|          110|          Accounting|
|       null|         null|            Treasury|
|       null|         null|       Corporate Tax|
|       null|         null|  Control And Credit|
|       null|         null|Shareholder Services|
|       null|         null|            Benefits|
|       null|         null|       Manufacturing|
|       null|         null|        Construction|
|       null|         null|         Contracting|
|       null|         null|          Operations|
|       null|         null|          IT Support|
|       null|         null|                 NOC|
|       null|         null|         IT Helpdesk|
|       null|         null|    Government Sales|
|       null|         null|        Retail Sales|
|       null|         null|          Recruiting|
|       null|         null|             Payroll|
+-----------+-------------+--------------------+



>>> empDf.alias("emp1").join(empDf.alias("emp2"), col("emp1.manager_id") == col("emp2.employee_id"), "inner").select(col("emp1.manager_id"), col("emp2.first_name"), col("emp2.last_name")).show(100)
+----------+----------+---------+
|manager_id|first_name|last_name|
+----------+----------+---------+
|       201|   Michael|Hartstein|
|       205|   Shelley|  Higgins|
|       100|    Steven|     King|
|       100|    Steven|     King|
|       100|    Steven|     King|
|       100|    Steven|     King|
|       100|    Steven|     King|
|       100|    Steven|     King|
|       100|    Steven|     King|
|       100|    Steven|     King|
|       100|    Steven|     King|
|       101|     Neena|  Kochhar|
|       101|     Neena|  Kochhar|
|       101|     Neena|  Kochhar|
|       101|     Neena|  Kochhar|
|       101|     Neena|  Kochhar|
|       102|       Lex|  De Haan|
|       103| Alexander|   Hunold|
|       103| Alexander|   Hunold|
|       103| Alexander|   Hunold|
|       103| Alexander|   Hunold|
|       108|     Nancy|Greenberg|
|       108|     Nancy|Greenberg|
|       108|     Nancy|Greenberg|
|       108|     Nancy|Greenberg|
|       108|     Nancy|Greenberg|
|       114|       Den| Raphaely|
|       114|       Den| Raphaely|
|       114|       Den| Raphaely|
|       114|       Den| Raphaely|
|       114|       Den| Raphaely|
|       120|   Matthew|    Weiss|
|       120|   Matthew|    Weiss|
|       120|   Matthew|    Weiss|
|       120|   Matthew|    Weiss|
|       121|      Adam|    Fripp|
|       121|      Adam|    Fripp|
|       121|      Adam|    Fripp|
|       121|      Adam|    Fripp|
|       122|     Payam| Kaufling|
|       122|     Payam| Kaufling|
|       122|     Payam| Kaufling|
|       122|     Payam| Kaufling|
|       123|    Shanta|  Vollman|
|       123|    Shanta|  Vollman|
|       123|    Shanta|  Vollman|
|       123|    Shanta|  Vollman|
|       124|     Kevin|  Mourgos|
|       124|     Kevin|  Mourgos|
+----------+----------+---------+



>>> empDf.alias("emp1").join(empDf.alias("emp2"), col("emp1.manager_id") == col("emp2.employee_id"), "inner").select(col("emp1.employee_id"), col("emp2.first_name"), col("emp2.last_name")).show(100)
+-----------+----------+---------+
|employee_id|first_name|last_name|
+-----------+----------+---------+
|        202|   Michael|Hartstein|
|        206|   Shelley|  Higgins|
|        124|    Steven|     King|
|        123|    Steven|     King|
|        122|    Steven|     King|
|        121|    Steven|     King|
|        120|    Steven|     King|
|        114|    Steven|     King|
|        102|    Steven|     King|
|        101|    Steven|     King|
|        201|    Steven|     King|
|        108|     Neena|  Kochhar|
|        205|     Neena|  Kochhar|
|        204|     Neena|  Kochhar|
|        203|     Neena|  Kochhar|
|        200|     Neena|  Kochhar|
|        103|       Lex|  De Haan|
|        107| Alexander|   Hunold|
|        106| Alexander|   Hunold|
|        105| Alexander|   Hunold|
|        104| Alexander|   Hunold|
|        113|     Nancy|Greenberg|
|        112|     Nancy|Greenberg|
|        111|     Nancy|Greenberg|
|        110|     Nancy|Greenberg|
|        109|     Nancy|Greenberg|
|        119|       Den| Raphaely|
|        118|       Den| Raphaely|
|        117|       Den| Raphaely|
|        116|       Den| Raphaely|
|        115|       Den| Raphaely|
|        128|   Matthew|    Weiss|
|        127|   Matthew|    Weiss|
|        126|   Matthew|    Weiss|
|        125|   Matthew|    Weiss|
|        132|      Adam|    Fripp|
|        131|      Adam|    Fripp|
|        130|      Adam|    Fripp|
|        129|      Adam|    Fripp|
|        136|     Payam| Kaufling|
|        135|     Payam| Kaufling|
|        134|     Payam| Kaufling|
|        133|     Payam| Kaufling|
|        140|    Shanta|  Vollman|
|        139|    Shanta|  Vollman|
|        138|    Shanta|  Vollman|
|        137|    Shanta|  Vollman|
|        199|     Kevin|  Mourgos|
|        198|     Kevin|  Mourgos|
+-----------+----------+---------+

>>> empDf.alias("emp1").join(empDf.alias("emp2"), col("emp1.manager_id") == col("emp2.employee_id"), "inner").select(col("emp1.manager_id"), col("emp2.first_name"), col("emp2.last_name")).dropDuplicates().show(100)
+----------+----------+---------+
|manager_id|first_name|last_name|
+----------+----------+---------+
|       122|     Payam| Kaufling|
|       101|     Neena|  Kochhar|
|       100|    Steven|     King|
|       205|   Shelley|  Higgins|
|       114|       Den| Raphaely|
|       103| Alexander|   Hunold|
|       124|     Kevin|  Mourgos|
|       120|   Matthew|    Weiss|
|       123|    Shanta|  Vollman|
|       121|      Adam|    Fripp|
|       108|     Nancy|Greenberg|
|       102|       Lex|  De Haan|
|       201|   Michael|Hartstein|
+----------+----------+---------+



>>> empDf.join(deptDf, (empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID) & (deptDf.LOCATION_ID==1700),"inner").select(empDf.EMPLOYEE_ID, empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME).show(100)
+-----------+-------------+---------------+
|EMPLOYEE_ID|DEPARTMENT_ID|DEPARTMENT_NAME|
+-----------+-------------+---------------+
|        200|           10| Administration|
|        119|           30|     Purchasing|
|        118|           30|     Purchasing|
|        117|           30|     Purchasing|
|        116|           30|     Purchasing|
|        115|           30|     Purchasing|
|        114|           30|     Purchasing|
|        102|           90|      Executive|
|        101|           90|      Executive|
|        100|           90|      Executive|
|        113|          100|        Finance|
|        112|          100|        Finance|
|        111|          100|        Finance|
|        110|          100|        Finance|
|        109|          100|        Finance|
|        108|          100|        Finance|
|        206|          110|     Accounting|
|        205|          110|     Accounting|
+-----------+-------------+---------------+




>>> from pyspark.sql.types import StructType,StructField, StringType, IntegerType
>>> location_data = [(1700,"INDIA"),(1800,"USA")]
>>> schema = StructType([ StructField("LOCATION_ID",IntegerType(),True), StructField("LOCATION_NAME", StringType(), True) ])
>>> locDf = spark.createDataFrame(data=location_data,schema=schema)
>>> locDf.printSchema()
root
 |-- LOCATION_ID: integer (nullable = true)
 |-- LOCATION_NAME: string (nullable = true)

>>> locDf.show()
+-----------+-------------+                                                     
|LOCATION_ID|LOCATION_NAME|
+-----------+-------------+
|       1700|        INDIA|
|       1800|          USA|
+-----------+-------------+



#this query is like 2 inner join
>>> empDf.join(deptDf, (empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID) & (deptDf.LOCATION_ID==1700),"inner").join(locDf,deptDf.LOCATION_ID == locDf.LOCATION_ID, "inner").select(empDf.EMPLOYEE_ID, empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME,locDf.LOCATION_NAME).show(100)
+-----------+-------------+---------------+-------------+
|EMPLOYEE_ID|DEPARTMENT_ID|DEPARTMENT_NAME|LOCATION_NAME|
+-----------+-------------+---------------+-------------+
|        205|          110|     Accounting|        INDIA|
|        206|          110|     Accounting|        INDIA|
|        108|          100|        Finance|        INDIA|
|        109|          100|        Finance|        INDIA|
|        110|          100|        Finance|        INDIA|
|        111|          100|        Finance|        INDIA|
|        112|          100|        Finance|        INDIA|
|        113|          100|        Finance|        INDIA|
|        100|           90|      Executive|        INDIA|
|        101|           90|      Executive|        INDIA|
|        102|           90|      Executive|        INDIA|
|        114|           30|     Purchasing|        INDIA|
|        115|           30|     Purchasing|        INDIA|
|        116|           30|     Purchasing|        INDIA|
|        117|           30|     Purchasing|        INDIA|
|        118|           30|     Purchasing|        INDIA|
|        119|           30|     Purchasing|        INDIA|
|        200|           10| Administration|        INDIA|
+-----------+-------------+---------------+-------------+


>>> deptDf = spark.read.option("header",True).option("inferSchema",True).csv("/input_data1/departments.csv")
>>> empDf = spark.read.option("header",True).option("inferSchema",True).csv("/input_data1/employees.csv")

>>> def upperCase(in_str):
...     out_str = in_str.upper()
...     return out_str
... 
>>> print(upperCase("hello"))
HELLO


>>> from pyspark.sql.functions import *
>>> from pyspark.sql.types import StructType,StructField, StringType, IntegerType
>>> upperCaseUDF = udf(lambda z : upperCase(z) , StringType())
>>> empDf.select(col("EMPLOYEE_ID") , col("FIRST_NAME"), col("LAST_NAME"), upperCaseUDF(col("FIRST_NAME")), upperCaseUDF(col("LAST_NAME"))).show()
+-----------+----------+---------+--------------------+-------------------+
|EMPLOYEE_ID|FIRST_NAME|LAST_NAME|<lambda>(FIRST_NAME)|<lambda>(LAST_NAME)|
+-----------+----------+---------+--------------------+-------------------+
|        198|    Donald| OConnell|              DONALD|           OCONNELL|
|        199|   Douglas|    Grant|             DOUGLAS|              GRANT|
|        200|  Jennifer|   Whalen|            JENNIFER|             WHALEN|
|        201|   Michael|Hartstein|             MICHAEL|          HARTSTEIN|
|        202|       Pat|      Fay|                 PAT|                FAY|
|        203|     Susan|   Mavris|               SUSAN|             MAVRIS|
|        204|   Hermann|     Baer|             HERMANN|               BAER|
|        205|   Shelley|  Higgins|             SHELLEY|            HIGGINS|
|        206|   William|    Gietz|             WILLIAM|              GIETZ|
|        100|    Steven|     King|              STEVEN|               KING|
|        101|     Neena|  Kochhar|               NEENA|            KOCHHAR|
|        102|       Lex|  De Haan|                 LEX|            DE HAAN|
|        103| Alexander|   Hunold|           ALEXANDER|             HUNOLD|
|        104|     Bruce|    Ernst|               BRUCE|              ERNST|
|        105|     David|   Austin|               DAVID|             AUSTIN|
|        106|     Valli|Pataballa|               VALLI|          PATABALLA|
|        107|     Diana|  Lorentz|               DIANA|            LORENTZ|
|        108|     Nancy|Greenberg|               NANCY|          GREENBERG|
|        109|    Daniel|   Faviet|              DANIEL|             FAVIET|
|        110|      John|     Chen|                JOHN|               CHEN|
+-----------+----------+---------+--------------------+-------------------+
only showing top 20 rows

>>> @udf(returnType=StringType())
... def upperCaseNew(in_str):
...     out_str = in_str.upper()
...     return out_str
... 
>>> empDf.select(col("EMPLOYEE_ID") , col("FIRST_NAME"), col("LAST_NAME"), upperCaseNew(col("FIRST_NAME")), upperCaseNew(col("LAST_NAME"))).show()
+-----------+----------+---------+------------------------+-----------------------+
|EMPLOYEE_ID|FIRST_NAME|LAST_NAME|upperCaseNew(FIRST_NAME)|upperCaseNew(LAST_NAME)|
+-----------+----------+---------+------------------------+-----------------------+
|        198|    Donald| OConnell|                  DONALD|               OCONNELL|
|        199|   Douglas|    Grant|                 DOUGLAS|                  GRANT|
|        200|  Jennifer|   Whalen|                JENNIFER|                 WHALEN|
|        201|   Michael|Hartstein|                 MICHAEL|              HARTSTEIN|
|        202|       Pat|      Fay|                     PAT|                    FAY|
|        203|     Susan|   Mavris|                   SUSAN|                 MAVRIS|
|        204|   Hermann|     Baer|                 HERMANN|                   BAER|
|        205|   Shelley|  Higgins|                 SHELLEY|                HIGGINS|
|        206|   William|    Gietz|                 WILLIAM|                  GIETZ|
|        100|    Steven|     King|                  STEVEN|                   KING|
|        101|     Neena|  Kochhar|                   NEENA|                KOCHHAR|
|        102|       Lex|  De Haan|                     LEX|                DE HAAN|
|        103| Alexander|   Hunold|               ALEXANDER|                 HUNOLD|
|        104|     Bruce|    Ernst|                   BRUCE|                  ERNST|
|        105|     David|   Austin|                   DAVID|                 AUSTIN|
|        106|     Valli|Pataballa|                   VALLI|              PATABALLA|
|        107|     Diana|  Lorentz|                   DIANA|                LORENTZ|
|        108|     Nancy|Greenberg|                   NANCY|              GREENBERG|
|        109|    Daniel|   Faviet|                  DANIEL|                 FAVIET|
|        110|      John|     Chen|                    JOHN|                   CHEN|
+-----------+----------+---------+------------------------+-----------------------+
only showing top 20 rows


>>> from pyspark.sql.window import Window
>>> windowSpec = Window.partitionBy("DEPARTMENT_ID").orderBy("SALARY")
>>> empDf.withColumn("salary_rank", rank().over(windowSpec)).select("DEPARTMENT_ID","SALARY","salary_rank").show(100)
+-------------+------+-----------+
|DEPARTMENT_ID|SALARY|salary_rank|
+-------------+------+-----------+
|           10|  4400|          1|
|           20|  6000|          1|
|           20| 13000|          2|
|           30|  2500|          1|
|           30|  2600|          2|
|           30|  2800|          3|
|           30|  2900|          4|
|           30|  3100|          5|
|           30| 11000|          6|
|           40|  6500|          1|
|           50|  2100|          1|
|           50|  2200|          2|
|           50|  2200|          2|
|           50|  2400|          4|
|           50|  2400|          4|
|           50|  2500|          6|
|           50|  2500|          6|
|           50|  2600|          8|
|           50|  2600|          8|
|           50|  2700|         10|
|           50|  2700|         10|
|           50|  2800|         12|
|           50|  2900|         13|
|           50|  3200|         14|
|           50|  3200|         14|
|           50|  3300|         16|
|           50|  3300|         16|
|           50|  3600|         18|
|           50|  5800|         19|
|           50|  6500|         20|
|           50|  7900|         21|
|           50|  8000|         22|
|           50|  8200|         23|
|           60|  4200|          1|
|           60|  4800|          2|
|           60|  4800|          2|
|           60|  6000|          4|
|           60|  9000|          5|
|           70| 10000|          1|
|           90| 17000|          1|
|           90| 17000|          1|
|           90| 24000|          3|
|          100|  6900|          1|
|          100|  7700|          2|
|          100|  7800|          3|
|          100|  8200|          4|
|          100|  9000|          5|
|          100| 12008|          6|
|          110|  8300|          1|
|          110| 12008|          2|
+-------------+------+-----------+

>>> windowSpec = Window.partitionBy("DEPARTMENT_ID").orderBy(col("SALARY").desc())
>>> empDf.withColumn("salary_rank", rank().over(windowSpec)).select("DEPARTMENT_ID","SALARY","salary_rank").show(100)
+-------------+------+-----------+
|DEPARTMENT_ID|SALARY|salary_rank|
+-------------+------+-----------+
|           10|  4400|          1|
|           20| 13000|          1|
|           20|  6000|          2|
|           30| 11000|          1|
|           30|  3100|          2|
|           30|  2900|          3|
|           30|  2800|          4|
|           30|  2600|          5|
|           30|  2500|          6|
|           40|  6500|          1|
|           50|  8200|          1|
|           50|  8000|          2|
|           50|  7900|          3|
|           50|  6500|          4|
|           50|  5800|          5|
|           50|  3600|          6|
|           50|  3300|          7|
|           50|  3300|          7|
|           50|  3200|          9|
|           50|  3200|          9|
|           50|  2900|         11|
|           50|  2800|         12|
|           50|  2700|         13|
|           50|  2700|         13|
|           50|  2600|         15|
|           50|  2600|         15|
|           50|  2500|         17|
|           50|  2500|         17|
|           50|  2400|         19|
|           50|  2400|         19|
|           50|  2200|         21|
|           50|  2200|         21|
|           50|  2100|         23|
|           60|  9000|          1|
|           60|  6000|          2|
|           60|  4800|          3|
|           60|  4800|          3|
|           60|  4200|          5|
|           70| 10000|          1|
|           90| 24000|          1|
|           90| 17000|          2|
|           90| 17000|          2|
|          100| 12008|          1|
|          100|  9000|          2|
|          100|  8200|          3|
|          100|  7800|          4|
|          100|  7700|          5|
|          100|  6900|          6|
|          110| 12008|          1|
|          110|  8300|          2|
+-------------+------+-----------+

>>> windowSpec = Window.partitionBy("DEPARTMENT_ID").orderBy(col("SALARY").desc())
>>> empDf.withColumn("SUM", sum("SALARY").over(windowSpec)).select("DEPARTMENT_ID","SALARY","SUM").show(100)
+-------------+------+-----+
|DEPARTMENT_ID|SALARY|  SUM|
+-------------+------+-----+
|           10|  4400| 4400|
|           20| 13000|13000|
|           20|  6000|19000|
|           30| 11000|11000|
|           30|  3100|14100|
|           30|  2900|17000|
|           30|  2800|19800|
|           30|  2600|22400|
|           30|  2500|24900|
|           40|  6500| 6500|
|           50|  8200| 8200|
|           50|  8000|16200|
|           50|  7900|24100|
|           50|  6500|30600|
|           50|  5800|36400|
|           50|  3600|40000|
|           50|  3300|46600|
|           50|  3300|46600|
|           50|  3200|53000|
|           50|  3200|53000|
|           50|  2900|55900|
|           50|  2800|58700|
|           50|  2700|64100|
|           50|  2700|64100|
|           50|  2600|69300|
|           50|  2600|69300|
|           50|  2500|74300|
|           50|  2500|74300|
|           50|  2400|79100|
|           50|  2400|79100|
|           50|  2200|83500|
|           50|  2200|83500|
|           50|  2100|85600|
|           60|  9000| 9000|
|           60|  6000|15000|
|           60|  4800|24600|
|           60|  4800|24600|
|           60|  4200|28800|
|           70| 10000|10000|
|           90| 24000|24000|
|           90| 17000|58000|
|           90| 17000|58000|
|          100| 12008|12008|
|          100|  9000|21008|
|          100|  8200|29208|
|          100|  7800|37008|
|          100|  7700|44708|
|          100|  6900|51608|
|          110| 12008|12008|
|          110|  8300|20308|
+-------------+------+-----+

>>> windowSpec = Window.partitionBy("DEPARTMENT_ID")
>>> empDf.withColumn("SUM", sum("SALARY").over(windowSpec)).select("DEPARTMENT_ID","SALARY","SUM").show(100)
+-------------+------+-----+
|DEPARTMENT_ID|SALARY|  SUM|
+-------------+------+-----+
|           10|  4400| 4400|
|           20| 13000|19000|
|           20|  6000|19000|
|           30| 11000|24900|
|           30|  3100|24900|
|           30|  2900|24900|
|           30|  2800|24900|
|           30|  2600|24900|
|           30|  2500|24900|
|           40|  6500| 6500|
|           50|  2600|85600|
|           50|  2600|85600|
|           50|  8000|85600|
|           50|  8200|85600|
|           50|  7900|85600|
|           50|  6500|85600|
|           50|  5800|85600|
|           50|  3200|85600|
|           50|  2700|85600|
|           50|  2400|85600|
|           50|  2200|85600|
|           50|  3300|85600|
|           50|  2800|85600|
|           50|  2500|85600|
|           50|  2100|85600|
|           50|  3300|85600|
|           50|  2900|85600|
|           50|  2400|85600|
|           50|  2200|85600|
|           50|  3600|85600|
|           50|  3200|85600|
|           50|  2700|85600|
|           50|  2500|85600|
|           60|  9000|28800|
|           60|  6000|28800|
|           60|  4800|28800|
|           60|  4800|28800|
|           60|  4200|28800|
|           70| 10000|10000|
|           90| 24000|58000|
|           90| 17000|58000|
|           90| 17000|58000|
|          100| 12008|51608|
|          100|  9000|51608|
|          100|  8200|51608|
|          100|  7700|51608|
|          100|  7800|51608|
|          100|  6900|51608|
|          110| 12008|20308|
|          110|  8300|20308|
+-------------+------+-----+