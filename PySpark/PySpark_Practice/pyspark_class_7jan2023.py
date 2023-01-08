abc@fdc009f06feb:~/workspace$ pyspark

>>> from pyspark.sql.types import StructType,StructField, StringType, IntegerType
>>> person_list = [("Berry","","Allen",1,"M"),
...         ("Oliver","Queen","",2,"M"),
...         ("Robert","","Williams",3,"M"),
...         ("Tony","","Stark",4,"F"),
...         ("Rajiv","Mary","Kumar",5,"F")
...     ]
>>> schema = StructType([ 
... StructField("firstname",StringType(),True),
... StructField("middlename",StringType(),True),
... StructField("lastname",StringType(),True),
... StructField("id", IntegerType(), True),
... StructField("gender", StringType(), True)])

>>> df = spark.createDataFrame(data=person_list,schema=schema)
>>> df.show()
+---------+----------+--------+---+------+                                      
|firstname|middlename|lastname| id|gender|
+---------+----------+--------+---+------+
|    Berry|          |   Allen|  1|     M|
|   Oliver|     Queen|        |  2|     M|
|   Robert|          |Williams|  3|     M|
|     Tony|          |   Stark|  4|     F|
|    Rajiv|      Mary|   Kumar|  5|     F|
+---------+----------+--------+---+------+

>>> df.show(truncate=False)
+---------+----------+--------+---+------+
|firstname|middlename|lastname|id |gender|
+---------+----------+--------+---+------+
|Berry    |          |Allen   |1  |M     |
|Oliver   |Queen     |        |2  |M     |
|Robert   |          |Williams|3  |M     |
|Tony     |          |Stark   |4  |F     |
|Rajiv    |Mary      |Kumar   |5  |F     |
+---------+----------+--------+---+------+

>>> df.printSchema()
root
 |-- firstname: string (nullable = true)
 |-- middlename: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- id: integer (nullable = true)
 |-- gender: string (nullable = true)



#fread data from hdfs departments.csv

>>> df1 = spark.read.option("header",True).csv("/input_data/departments.csv")
>>> df1.printSchema()                                                           
root
 |-- DEPARTMENT_ID: string (nullable = true)
 |-- DEPARTMENT_NAME: string (nullable = true)
 |-- MANAGER_ID: string (nullable = true)
 |-- LOCATION_ID: string (nullable = true)

>>> df1.show()
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

>>> df2 = spark.read.option("header",True).option("inferSchema",True).csv("/input_data/departments.csv")
>>> df2.printSchema()
root
 |-- DEPARTMENT_ID: integer (nullable = true)
 |-- DEPARTMENT_NAME: string (nullable = true)
 |-- MANAGER_ID: string (nullable = true)
 |-- LOCATION_ID: integer (nullable = true)


>>> df2.show()
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

>>> empDf = spark.read.option("header",True).option("inferSchema",True).csv("/input_data/employees.csv")
>>> empDf.printSchema()
root
 |-- EMPLOYEE_ID: integer (nullable = true)
 |-- FIRST_NAME: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- PHONE_NUMBER: string (nullable = true)
 |-- HIRE_DATE: string (nullable = true)
 |-- JOB_ID: string (nullable = true)
 |-- SALARY: integer (nullable = true)
 |-- COMMISSION_PCT: string (nullable = true)
 |-- MANAGER_ID: string (nullable = true)
 |-- DEPARTMENT_ID: integer (nullable = true)


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


>>> df_tmp = empDf.select("*")
>>> df_tmp.show()
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


>>> empDf.select("*").show()
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


>>> empDf.select("EMPLOYEE_ID","FIRST_NAME").show()
+-----------+----------+
|EMPLOYEE_ID|FIRST_NAME|
+-----------+----------+
|        198|    Donald|
|        199|   Douglas|
|        200|  Jennifer|
|        201|   Michael|
|        202|       Pat|
|        203|     Susan|
|        204|   Hermann|
|        205|   Shelley|
|        206|   William|
|        100|    Steven|
|        101|     Neena|
|        102|       Lex|
|        103| Alexander|
|        104|     Bruce|
|        105|     David|
|        106|     Valli|
|        107|     Diana|
|        108|     Nancy|
|        109|    Daniel|
|        110|      John|
+-----------+----------+
only showing top 20 rows


>>> empDf.select(empDf.EMPLOYEE_ID,empDf.FIRST_NAME).show()
+-----------+----------+
|EMPLOYEE_ID|FIRST_NAME|
+-----------+----------+
|        198|    Donald|
|        199|   Douglas|
|        200|  Jennifer|
|        201|   Michael|
|        202|       Pat|
|        203|     Susan|
|        204|   Hermann|
|        205|   Shelley|
|        206|   William|
|        100|    Steven|
|        101|     Neena|
|        102|       Lex|
|        103| Alexander|
|        104|     Bruce|
|        105|     David|
|        106|     Valli|
|        107|     Diana|
|        108|     Nancy|
|        109|    Daniel|
|        110|      John|
+-----------+----------+
only showing top 20 rows


>>> empDf.select(empDf["EMPLOYEE_ID"],empDf["FIRST_NAME"]).show()
+-----------+----------+
|EMPLOYEE_ID|FIRST_NAME|
+-----------+----------+
|        198|    Donald|
|        199|   Douglas|
|        200|  Jennifer|
|        201|   Michael|
|        202|       Pat|
|        203|     Susan|
|        204|   Hermann|
|        205|   Shelley|
|        206|   William|
|        100|    Steven|
|        101|     Neena|
|        102|       Lex|
|        103| Alexander|
|        104|     Bruce|
|        105|     David|
|        106|     Valli|
|        107|     Diana|
|        108|     Nancy|
|        109|    Daniel|
|        110|      John|
+-----------+----------+
only showing top 20 rows


>>> from pyspark.sql.functions import col
>>> empDf.select(col("EMPLOYEE_ID"),col("FIRST_NAME")).show()
+-----------+----------+
|EMPLOYEE_ID|FIRST_NAME|
+-----------+----------+
|        198|    Donald|
|        199|   Douglas|
|        200|  Jennifer|
|        201|   Michael|
|        202|       Pat|
|        203|     Susan|
|        204|   Hermann|
|        205|   Shelley|
|        206|   William|
|        100|    Steven|
|        101|     Neena|
|        102|       Lex|
|        103| Alexander|
|        104|     Bruce|
|        105|     David|
|        106|     Valli|
|        107|     Diana|
|        108|     Nancy|
|        109|    Daniel|
|        110|      John|
+-----------+----------+
only showing top 20 rows


>>> empDf.select(col("EMPLOYEE_ID").alias("EMP_ID"),col("FIRST_NAME").alias("F_NAME")).show()
+------+---------+
|EMP_ID|   F_NAME|
+------+---------+
|   198|   Donald|
|   199|  Douglas|
|   200| Jennifer|
|   201|  Michael|
|   202|      Pat|
|   203|    Susan|
|   204|  Hermann|
|   205|  Shelley|
|   206|  William|
|   100|   Steven|
|   101|    Neena|
|   102|      Lex|
|   103|Alexander|
|   104|    Bruce|
|   105|    David|
|   106|    Valli|
|   107|    Diana|
|   108|    Nancy|
|   109|   Daniel|
|   110|     John|
+------+---------+
only showing top 20 rows

>>> empDf.select("EMPLOYEE_ID","FIRST_NAME","SALARY").withColumn("NEW_SALARY",col("SALARY")+1000).show()
+-----------+----------+------+----------+
|EMPLOYEE_ID|FIRST_NAME|SALARY|NEW_SALARY|
+-----------+----------+------+----------+
|        198|    Donald|  2600|      3600|
|        199|   Douglas|  2600|      3600|
|        200|  Jennifer|  4400|      5400|
|        201|   Michael| 13000|     14000|
|        202|       Pat|  6000|      7000|
|        203|     Susan|  6500|      7500|
|        204|   Hermann| 10000|     11000|
|        205|   Shelley| 12008|     13008|
|        206|   William|  8300|      9300|
|        100|    Steven| 24000|     25000|
|        101|     Neena| 17000|     18000|
|        102|       Lex| 17000|     18000|
|        103| Alexander|  9000|     10000|
|        104|     Bruce|  6000|      7000|
|        105|     David|  4800|      5800|
|        106|     Valli|  4800|      5800|
|        107|     Diana|  4200|      5200|
|        108|     Nancy| 12008|     13008|
|        109|    Daniel|  9000|     10000|
|        110|      John|  8200|      9200|
+-----------+----------+------+----------+
only showing top 20 rows


>>> empDf.withColumn("NEW_SALARY",col("SALARY")+1000).select("EMPLOYEE_ID","FIRST_NAME","NEW_SALARY").show()
+-----------+----------+----------+
|EMPLOYEE_ID|FIRST_NAME|NEW_SALARY|
+-----------+----------+----------+
|        198|    Donald|      3600|
|        199|   Douglas|      3600|
|        200|  Jennifer|      5400|
|        201|   Michael|     14000|
|        202|       Pat|      7000|
|        203|     Susan|      7500|
|        204|   Hermann|     11000|
|        205|   Shelley|     13008|
|        206|   William|      9300|
|        100|    Steven|     25000|
|        101|     Neena|     18000|
|        102|       Lex|     18000|
|        103| Alexander|     10000|
|        104|     Bruce|      7000|
|        105|     David|      5800|
|        106|     Valli|      5800|
|        107|     Diana|      5200|
|        108|     Nancy|     13008|
|        109|    Daniel|     10000|
|        110|      John|      9200|
+-----------+----------+----------+
only showing top 20 rows

#to update existing column
>>> empDf.withColumn("SALARY",col("SALARY") - 1000).select("EMPLOYEE_ID","FIRST_NAME","SALARY").show()
+-----------+----------+------+
|EMPLOYEE_ID|FIRST_NAME|SALARY|
+-----------+----------+------+
|        198|    Donald|  1600|
|        199|   Douglas|  1600|
|        200|  Jennifer|  3400|
|        201|   Michael| 12000|
|        202|       Pat|  5000|
|        203|     Susan|  5500|
|        204|   Hermann|  9000|
|        205|   Shelley| 11008|
|        206|   William|  7300|
|        100|    Steven| 23000|
|        101|     Neena| 16000|
|        102|       Lex| 16000|
|        103| Alexander|  8000|
|        104|     Bruce|  5000|
|        105|     David|  3800|
|        106|     Valli|  3800|
|        107|     Diana|  3200|
|        108|     Nancy| 11008|
|        109|    Daniel|  8000|
|        110|      John|  7200|
+-----------+----------+------+
only showing top 20 rows


>>> empDf.withColumnRenamed("SALARY","EMP_SALARY").show()
+-----------+----------+---------+--------+------------+---------+----------+----------+--------------+----------+-------------+
|EMPLOYEE_ID|FIRST_NAME|LAST_NAME|   EMAIL|PHONE_NUMBER|HIRE_DATE|    JOB_ID|EMP_SALARY|COMMISSION_PCT|MANAGER_ID|DEPARTMENT_ID|
+-----------+----------+---------+--------+------------+---------+----------+----------+--------------+----------+-------------+
|        198|    Donald| OConnell|DOCONNEL|650.507.9833|21-JUN-07|  SH_CLERK|      2600|            - |       124|           50|
|        199|   Douglas|    Grant|  DGRANT|650.507.9844|13-JAN-08|  SH_CLERK|      2600|            - |       124|           50|
|        200|  Jennifer|   Whalen| JWHALEN|515.123.4444|17-SEP-03|   AD_ASST|      4400|            - |       101|           10|
|        201|   Michael|Hartstein|MHARTSTE|515.123.5555|17-FEB-04|    MK_MAN|     13000|            - |       100|           20|
|        202|       Pat|      Fay|    PFAY|603.123.6666|17-AUG-05|    MK_REP|      6000|            - |       201|           20|
|        203|     Susan|   Mavris| SMAVRIS|515.123.7777|07-JUN-02|    HR_REP|      6500|            - |       101|           40|
|        204|   Hermann|     Baer|   HBAER|515.123.8888|07-JUN-02|    PR_REP|     10000|            - |       101|           70|
|        205|   Shelley|  Higgins|SHIGGINS|515.123.8080|07-JUN-02|    AC_MGR|     12008|            - |       101|          110|
|        206|   William|    Gietz|  WGIETZ|515.123.8181|07-JUN-02|AC_ACCOUNT|      8300|            - |       205|          110|
|        100|    Steven|     King|   SKING|515.123.4567|17-JUN-03|   AD_PRES|     24000|            - |        - |           90|
|        101|     Neena|  Kochhar|NKOCHHAR|515.123.4568|21-SEP-05|     AD_VP|     17000|            - |       100|           90|
|        102|       Lex|  De Haan| LDEHAAN|515.123.4569|13-JAN-01|     AD_VP|     17000|            - |       100|           90|
|        103| Alexander|   Hunold| AHUNOLD|590.423.4567|03-JAN-06|   IT_PROG|      9000|            - |       102|           60|
|        104|     Bruce|    Ernst|  BERNST|590.423.4568|21-MAY-07|   IT_PROG|      6000|            - |       103|           60|
|        105|     David|   Austin| DAUSTIN|590.423.4569|25-JUN-05|   IT_PROG|      4800|            - |       103|           60|
|        106|     Valli|Pataballa|VPATABAL|590.423.4560|05-FEB-06|   IT_PROG|      4800|            - |       103|           60|
|        107|     Diana|  Lorentz|DLORENTZ|590.423.5567|07-FEB-07|   IT_PROG|      4200|            - |       103|           60|
|        108|     Nancy|Greenberg|NGREENBE|515.124.4569|17-AUG-02|    FI_MGR|     12008|            - |       101|          100|
|        109|    Daniel|   Faviet| DFAVIET|515.124.4169|16-AUG-02|FI_ACCOUNT|      9000|            - |       108|          100|
|        110|      John|     Chen|   JCHEN|515.124.4269|28-SEP-05|FI_ACCOUNT|      8200|            - |       108|          100|
+-----------+----------+---------+--------+------------+---------+----------+----------+--------------+----------+-------------+
only showing top 20 rows


>>> empDf.drop("COMMISSION_PCT").show()
+-----------+----------+---------+--------+------------+---------+----------+------+----------+-------------+
|EMPLOYEE_ID|FIRST_NAME|LAST_NAME|   EMAIL|PHONE_NUMBER|HIRE_DATE|    JOB_ID|SALARY|MANAGER_ID|DEPARTMENT_ID|
+-----------+----------+---------+--------+------------+---------+----------+------+----------+-------------+
|        198|    Donald| OConnell|DOCONNEL|650.507.9833|21-JUN-07|  SH_CLERK|  2600|       124|           50|
|        199|   Douglas|    Grant|  DGRANT|650.507.9844|13-JAN-08|  SH_CLERK|  2600|       124|           50|
|        200|  Jennifer|   Whalen| JWHALEN|515.123.4444|17-SEP-03|   AD_ASST|  4400|       101|           10|
|        201|   Michael|Hartstein|MHARTSTE|515.123.5555|17-FEB-04|    MK_MAN| 13000|       100|           20|
|        202|       Pat|      Fay|    PFAY|603.123.6666|17-AUG-05|    MK_REP|  6000|       201|           20|
|        203|     Susan|   Mavris| SMAVRIS|515.123.7777|07-JUN-02|    HR_REP|  6500|       101|           40|
|        204|   Hermann|     Baer|   HBAER|515.123.8888|07-JUN-02|    PR_REP| 10000|       101|           70|
|        205|   Shelley|  Higgins|SHIGGINS|515.123.8080|07-JUN-02|    AC_MGR| 12008|       101|          110|
|        206|   William|    Gietz|  WGIETZ|515.123.8181|07-JUN-02|AC_ACCOUNT|  8300|       205|          110|
|        100|    Steven|     King|   SKING|515.123.4567|17-JUN-03|   AD_PRES| 24000|        - |           90|
|        101|     Neena|  Kochhar|NKOCHHAR|515.123.4568|21-SEP-05|     AD_VP| 17000|       100|           90|
|        102|       Lex|  De Haan| LDEHAAN|515.123.4569|13-JAN-01|     AD_VP| 17000|       100|           90|
|        103| Alexander|   Hunold| AHUNOLD|590.423.4567|03-JAN-06|   IT_PROG|  9000|       102|           60|
|        104|     Bruce|    Ernst|  BERNST|590.423.4568|21-MAY-07|   IT_PROG|  6000|       103|           60|
|        105|     David|   Austin| DAUSTIN|590.423.4569|25-JUN-05|   IT_PROG|  4800|       103|           60|
|        106|     Valli|Pataballa|VPATABAL|590.423.4560|05-FEB-06|   IT_PROG|  4800|       103|           60|
|        107|     Diana|  Lorentz|DLORENTZ|590.423.5567|07-FEB-07|   IT_PROG|  4200|       103|           60|
|        108|     Nancy|Greenberg|NGREENBE|515.124.4569|17-AUG-02|    FI_MGR| 12008|       101|          100|
|        109|    Daniel|   Faviet| DFAVIET|515.124.4169|16-AUG-02|FI_ACCOUNT|  9000|       108|          100|
|        110|      John|     Chen|   JCHEN|515.124.4269|28-SEP-05|FI_ACCOUNT|  8200|       108|          100|
+-----------+----------+---------+--------+------------+---------+----------+------+----------+-------------+
only showing top 20 rows


>>> empDf.filter(col("SALARY") < 5000).show()
+-----------+----------+-----------+--------+------------+---------+--------+------+--------------+----------+-------------+
|EMPLOYEE_ID|FIRST_NAME|  LAST_NAME|   EMAIL|PHONE_NUMBER|HIRE_DATE|  JOB_ID|SALARY|COMMISSION_PCT|MANAGER_ID|DEPARTMENT_ID|
+-----------+----------+-----------+--------+------------+---------+--------+------+--------------+----------+-------------+
|        198|    Donald|   OConnell|DOCONNEL|650.507.9833|21-JUN-07|SH_CLERK|  2600|            - |       124|           50|
|        199|   Douglas|      Grant|  DGRANT|650.507.9844|13-JAN-08|SH_CLERK|  2600|            - |       124|           50|
|        200|  Jennifer|     Whalen| JWHALEN|515.123.4444|17-SEP-03| AD_ASST|  4400|            - |       101|           10|
|        105|     David|     Austin| DAUSTIN|590.423.4569|25-JUN-05| IT_PROG|  4800|            - |       103|           60|
|        106|     Valli|  Pataballa|VPATABAL|590.423.4560|05-FEB-06| IT_PROG|  4800|            - |       103|           60|
|        107|     Diana|    Lorentz|DLORENTZ|590.423.5567|07-FEB-07| IT_PROG|  4200|            - |       103|           60|
|        115| Alexander|       Khoo|   AKHOO|515.127.4562|18-MAY-03|PU_CLERK|  3100|            - |       114|           30|
|        116|    Shelli|      Baida|  SBAIDA|515.127.4563|24-DEC-05|PU_CLERK|  2900|            - |       114|           30|
|        117|     Sigal|     Tobias| STOBIAS|515.127.4564|24-JUL-05|PU_CLERK|  2800|            - |       114|           30|
|        118|       Guy|     Himuro| GHIMURO|515.127.4565|15-NOV-06|PU_CLERK|  2600|            - |       114|           30|
|        119|     Karen| Colmenares|KCOLMENA|515.127.4566|10-AUG-07|PU_CLERK|  2500|            - |       114|           30|
|        125|     Julia|      Nayer|  JNAYER|650.124.1214|16-JUL-05|ST_CLERK|  3200|            - |       120|           50|
|        126|     Irene|Mikkilineni|IMIKKILI|650.124.1224|28-SEP-06|ST_CLERK|  2700|            - |       120|           50|
|        127|     James|     Landry| JLANDRY|650.124.1334|14-JAN-07|ST_CLERK|  2400|            - |       120|           50|
|        128|    Steven|     Markle| SMARKLE|650.124.1434|08-MAR-08|ST_CLERK|  2200|            - |       120|           50|
|        129|     Laura|     Bissot| LBISSOT|650.124.5234|20-AUG-05|ST_CLERK|  3300|            - |       121|           50|
|        130|     Mozhe|   Atkinson|MATKINSO|650.124.6234|30-OCT-05|ST_CLERK|  2800|            - |       121|           50|
|        131|     James|     Marlow| JAMRLOW|650.124.7234|16-FEB-05|ST_CLERK|  2500|            - |       121|           50|
|        132|        TJ|      Olson| TJOLSON|650.124.8234|10-APR-07|ST_CLERK|  2100|            - |       121|           50|
|        133|     Jason|     Mallin| JMALLIN|650.127.1934|14-JUN-04|ST_CLERK|  3300|            - |       122|           50|
+-----------+----------+-----------+--------+------------+---------+--------+------+--------------+----------+-------------+
only showing top 20 rows


>>> empDf.filter(col("SALARY") < 5000).select("EMPLOYEE_ID","FIRST_NAME","SALARY").show()
+-----------+----------+------+
|EMPLOYEE_ID|FIRST_NAME|SALARY|
+-----------+----------+------+
|        198|    Donald|  2600|
|        199|   Douglas|  2600|
|        200|  Jennifer|  4400|
|        105|     David|  4800|
|        106|     Valli|  4800|
|        107|     Diana|  4200|
|        115| Alexander|  3100|
|        116|    Shelli|  2900|
|        117|     Sigal|  2800|
|        118|       Guy|  2600|
|        119|     Karen|  2500|
|        125|     Julia|  3200|
|        126|     Irene|  2700|
|        127|     James|  2400|
|        128|    Steven|  2200|
|        129|     Laura|  3300|
|        130|     Mozhe|  2800|
|        131|     James|  2500|
|        132|        TJ|  2100|
|        133|     Jason|  3300|
+-----------+----------+------+
only showing top 20 rows


>>> empDf.filter((col("DEPARTMENT_ID") == 50) & (col("SALARY") < 5000) ).select("EMPLOYEE_ID","FIRST_NAME","SALARY","DEPARTMENT_ID").show()
+-----------+----------+------+-------------+
|EMPLOYEE_ID|FIRST_NAME|SALARY|DEPARTMENT_ID|
+-----------+----------+------+-------------+
|        198|    Donald|  2600|           50|
|        199|   Douglas|  2600|           50|
|        125|     Julia|  3200|           50|
|        126|     Irene|  2700|           50|
|        127|     James|  2400|           50|
|        128|    Steven|  2200|           50|
|        129|     Laura|  3300|           50|
|        130|     Mozhe|  2800|           50|
|        131|     James|  2500|           50|
|        132|        TJ|  2100|           50|
|        133|     Jason|  3300|           50|
|        134|   Michael|  2900|           50|
|        135|        Ki|  2400|           50|
|        136|     Hazel|  2200|           50|
|        137|    Renske|  3600|           50|
|        138|   Stephen|  3200|           50|
|        139|      John|  2700|           50|
|        140|    Joshua|  2500|           50|
+-----------+----------+------+-------------+

>>> empDf.filter("DEPARTMENT_ID <> 50").select("EMPLOYEE_ID","FIRST_NAME","SALARY","DEPARTMENT_ID").show()
+-----------+-----------+------+-------------+
|EMPLOYEE_ID| FIRST_NAME|SALARY|DEPARTMENT_ID|
+-----------+-----------+------+-------------+
|        200|   Jennifer|  4400|           10|
|        201|    Michael| 13000|           20|
|        202|        Pat|  6000|           20|
|        203|      Susan|  6500|           40|
|        204|    Hermann| 10000|           70|
|        205|    Shelley| 12008|          110|
|        206|    William|  8300|          110|
|        100|     Steven| 24000|           90|
|        101|      Neena| 17000|           90|
|        102|        Lex| 17000|           90|
|        103|  Alexander|  9000|           60|
|        104|      Bruce|  6000|           60|
|        105|      David|  4800|           60|
|        106|      Valli|  4800|           60|
|        107|      Diana|  4200|           60|
|        108|      Nancy| 12008|          100|
|        109|     Daniel|  9000|          100|
|        110|       John|  8200|          100|
|        111|     Ismael|  7700|          100|
|        112|Jose Manuel|  7800|          100|
+-----------+-----------+------+-------------+
only showing top 20 rows


>>> empDf.filter("DEPARTMENT_ID == 50 and SALARY < 5000" ).select("EMPLOYEE_ID","FIRST_NAME","SALARY","DEPARTMENT_ID").show()
+-----------+----------+------+-------------+
|EMPLOYEE_ID|FIRST_NAME|SALARY|DEPARTMENT_ID|
+-----------+----------+------+-------------+
|        198|    Donald|  2600|           50|
|        199|   Douglas|  2600|           50|
|        125|     Julia|  3200|           50|
|        126|     Irene|  2700|           50|
|        127|     James|  2400|           50|
|        128|    Steven|  2200|           50|
|        129|     Laura|  3300|           50|
|        130|     Mozhe|  2800|           50|
|        131|     James|  2500|           50|
|        132|        TJ|  2100|           50|
|        133|     Jason|  3300|           50|
|        134|   Michael|  2900|           50|
|        135|        Ki|  2400|           50|
|        136|     Hazel|  2200|           50|
|        137|    Renske|  3600|           50|
|        138|   Stephen|  3200|           50|
|        139|      John|  2700|           50|
|        140|    Joshua|  2500|           50|
+-----------+----------+------+-------------+


>>> empDf.distinct().show(100)                                                  
+-----------+-----------+-----------+--------+------------+---------+----------+------+--------------+----------+-------------+
|EMPLOYEE_ID| FIRST_NAME|  LAST_NAME|   EMAIL|PHONE_NUMBER|HIRE_DATE|    JOB_ID|SALARY|COMMISSION_PCT|MANAGER_ID|DEPARTMENT_ID|
+-----------+-----------+-----------+--------+------------+---------+----------+------+--------------+----------+-------------+
|        120|    Matthew|      Weiss|  MWEISS|650.123.1234|18-JUL-04|    ST_MAN|  8000|            - |       100|           50|
|        118|        Guy|     Himuro| GHIMURO|515.127.4565|15-NOV-06|  PU_CLERK|  2600|            - |       114|           30|
|        110|       John|       Chen|   JCHEN|515.124.4269|28-SEP-05|FI_ACCOUNT|  8200|            - |       108|          100|
|        123|     Shanta|    Vollman|SVOLLMAN|650.123.4234|10-OCT-05|    ST_MAN|  6500|            - |       100|           50|
|        124|      Kevin|    Mourgos|KMOURGOS|650.123.5234|16-NOV-07|    ST_MAN|  5800|            - |       100|           50|
|        137|     Renske|     Ladwig| RLADWIG|650.121.1234|14-JUL-03|  ST_CLERK|  3600|            - |       123|           50|
|        132|         TJ|      Olson| TJOLSON|650.124.8234|10-APR-07|  ST_CLERK|  2100|            - |       121|           50|
|        113|       Luis|       Popp|   LPOPP|515.124.4567|07-DEC-07|FI_ACCOUNT|  6900|            - |       108|          100|
|        139|       John|        Seo|    JSEO|650.121.2019|12-FEB-06|  ST_CLERK|  2700|            - |       123|           50|
|        201|    Michael|  Hartstein|MHARTSTE|515.123.5555|17-FEB-04|    MK_MAN| 13000|            - |       100|           20|
|        107|      Diana|    Lorentz|DLORENTZ|590.423.5567|07-FEB-07|   IT_PROG|  4200|            - |       103|           60|
|        135|         Ki|        Gee|    KGEE|650.127.1734|12-DEC-07|  ST_CLERK|  2400|            - |       122|           50|
|        104|      Bruce|      Ernst|  BERNST|590.423.4568|21-MAY-07|   IT_PROG|  6000|            - |       103|           60|
|        103|  Alexander|     Hunold| AHUNOLD|590.423.4567|03-JAN-06|   IT_PROG|  9000|            - |       102|           60|
|        108|      Nancy|  Greenberg|NGREENBE|515.124.4569|17-AUG-02|    FI_MGR| 12008|            - |       101|          100|
|        121|       Adam|      Fripp|  AFRIPP|650.123.2234|10-APR-05|    ST_MAN|  8200|            - |       100|           50|
|        100|     Steven|       King|   SKING|515.123.4567|17-JUN-03|   AD_PRES| 24000|            - |        - |           90|
|        117|      Sigal|     Tobias| STOBIAS|515.127.4564|24-JUL-05|  PU_CLERK|  2800|            - |       114|           30|
|        130|      Mozhe|   Atkinson|MATKINSO|650.124.6234|30-OCT-05|  ST_CLERK|  2800|            - |       121|           50|
|        134|    Michael|     Rogers| MROGERS|650.127.1834|26-AUG-06|  ST_CLERK|  2900|            - |       122|           50|
|        133|      Jason|     Mallin| JMALLIN|650.127.1934|14-JUN-04|  ST_CLERK|  3300|            - |       122|           50|
|        138|    Stephen|     Stiles| SSTILES|650.121.2034|26-OCT-05|  ST_CLERK|  3200|            - |       123|           50|
|        105|      David|     Austin| DAUSTIN|590.423.4569|25-JUN-05|   IT_PROG|  4800|            - |       103|           60|
|        111|     Ismael|    Sciarra|ISCIARRA|515.124.4369|30-SEP-05|FI_ACCOUNT|  7700|            - |       108|          100|
|        116|     Shelli|      Baida|  SBAIDA|515.127.4563|24-DEC-05|  PU_CLERK|  2900|            - |       114|           30|
|        204|    Hermann|       Baer|   HBAER|515.123.8888|07-JUN-02|    PR_REP| 10000|            - |       101|           70|
|        115|  Alexander|       Khoo|   AKHOO|515.127.4562|18-MAY-03|  PU_CLERK|  3100|            - |       114|           30|
|        102|        Lex|    De Haan| LDEHAAN|515.123.4569|13-JAN-01|     AD_VP| 17000|            - |       100|           90|
|        114|        Den|   Raphaely|DRAPHEAL|515.127.4561|07-DEC-02|    PU_MAN| 11000|            - |       100|           30|
|        206|    William|      Gietz|  WGIETZ|515.123.8181|07-JUN-02|AC_ACCOUNT|  8300|            - |       205|          110|
|        205|    Shelley|    Higgins|SHIGGINS|515.123.8080|07-JUN-02|    AC_MGR| 12008|            - |       101|          110|
|        119|      Karen| Colmenares|KCOLMENA|515.127.4566|10-AUG-07|  PU_CLERK|  2500|            - |       114|           30|
|        106|      Valli|  Pataballa|VPATABAL|590.423.4560|05-FEB-06|   IT_PROG|  4800|            - |       103|           60|
|        126|      Irene|Mikkilineni|IMIKKILI|650.124.1224|28-SEP-06|  ST_CLERK|  2700|            - |       120|           50|
|        140|     Joshua|      Patel|  JPATEL|650.121.1834|06-APR-06|  ST_CLERK|  2500|            - |       123|           50|
|        125|      Julia|      Nayer|  JNAYER|650.124.1214|16-JUL-05|  ST_CLERK|  3200|            - |       120|           50|
|        136|      Hazel| Philtanker|HPHILTAN|650.127.1634|06-FEB-08|  ST_CLERK|  2200|            - |       122|           50|
|        129|      Laura|     Bissot| LBISSOT|650.124.5234|20-AUG-05|  ST_CLERK|  3300|            - |       121|           50|
|        203|      Susan|     Mavris| SMAVRIS|515.123.7777|07-JUN-02|    HR_REP|  6500|            - |       101|           40|
|        198|     Donald|   OConnell|DOCONNEL|650.507.9833|21-JUN-07|  SH_CLERK|  2600|            - |       124|           50|
|        202|        Pat|        Fay|    PFAY|603.123.6666|17-AUG-05|    MK_REP|  6000|            - |       201|           20|
|        200|   Jennifer|     Whalen| JWHALEN|515.123.4444|17-SEP-03|   AD_ASST|  4400|            - |       101|           10|
|        109|     Daniel|     Faviet| DFAVIET|515.124.4169|16-AUG-02|FI_ACCOUNT|  9000|            - |       108|          100|
|        101|      Neena|    Kochhar|NKOCHHAR|515.123.4568|21-SEP-05|     AD_VP| 17000|            - |       100|           90|
|        122|      Payam|   Kaufling|PKAUFLIN|650.123.3234|01-MAY-03|    ST_MAN|  7900|            - |       100|           50|
|        199|    Douglas|      Grant|  DGRANT|650.507.9844|13-JAN-08|  SH_CLERK|  2600|            - |       124|           50|
|        127|      James|     Landry| JLANDRY|650.124.1334|14-JAN-07|  ST_CLERK|  2400|            - |       120|           50|
|        128|     Steven|     Markle| SMARKLE|650.124.1434|08-MAR-08|  ST_CLERK|  2200|            - |       120|           50|
|        112|Jose Manuel|      Urman| JMURMAN|515.124.4469|07-MAR-06|FI_ACCOUNT|  7800|            - |       108|          100|
|        131|      James|     Marlow| JAMRLOW|650.124.7234|16-FEB-05|  ST_CLERK|  2500|            - |       121|           50|
+-----------+-----------+-----------+--------+------------+---------+----------+------+--------------+----------+-------------+


>>> empDf.dropDuplicates().show(100)
+-----------+-----------+-----------+--------+------------+---------+----------+------+--------------+----------+-------------+
|EMPLOYEE_ID| FIRST_NAME|  LAST_NAME|   EMAIL|PHONE_NUMBER|HIRE_DATE|    JOB_ID|SALARY|COMMISSION_PCT|MANAGER_ID|DEPARTMENT_ID|
+-----------+-----------+-----------+--------+------------+---------+----------+------+--------------+----------+-------------+
|        120|    Matthew|      Weiss|  MWEISS|650.123.1234|18-JUL-04|    ST_MAN|  8000|            - |       100|           50|
|        118|        Guy|     Himuro| GHIMURO|515.127.4565|15-NOV-06|  PU_CLERK|  2600|            - |       114|           30|
|        110|       John|       Chen|   JCHEN|515.124.4269|28-SEP-05|FI_ACCOUNT|  8200|            - |       108|          100|
|        123|     Shanta|    Vollman|SVOLLMAN|650.123.4234|10-OCT-05|    ST_MAN|  6500|            - |       100|           50|
|        124|      Kevin|    Mourgos|KMOURGOS|650.123.5234|16-NOV-07|    ST_MAN|  5800|            - |       100|           50|
|        137|     Renske|     Ladwig| RLADWIG|650.121.1234|14-JUL-03|  ST_CLERK|  3600|            - |       123|           50|
|        132|         TJ|      Olson| TJOLSON|650.124.8234|10-APR-07|  ST_CLERK|  2100|            - |       121|           50|
|        113|       Luis|       Popp|   LPOPP|515.124.4567|07-DEC-07|FI_ACCOUNT|  6900|            - |       108|          100|
|        139|       John|        Seo|    JSEO|650.121.2019|12-FEB-06|  ST_CLERK|  2700|            - |       123|           50|
|        201|    Michael|  Hartstein|MHARTSTE|515.123.5555|17-FEB-04|    MK_MAN| 13000|            - |       100|           20|
|        107|      Diana|    Lorentz|DLORENTZ|590.423.5567|07-FEB-07|   IT_PROG|  4200|            - |       103|           60|
|        135|         Ki|        Gee|    KGEE|650.127.1734|12-DEC-07|  ST_CLERK|  2400|            - |       122|           50|
|        104|      Bruce|      Ernst|  BERNST|590.423.4568|21-MAY-07|   IT_PROG|  6000|            - |       103|           60|
|        103|  Alexander|     Hunold| AHUNOLD|590.423.4567|03-JAN-06|   IT_PROG|  9000|            - |       102|           60|
|        108|      Nancy|  Greenberg|NGREENBE|515.124.4569|17-AUG-02|    FI_MGR| 12008|            - |       101|          100|
|        121|       Adam|      Fripp|  AFRIPP|650.123.2234|10-APR-05|    ST_MAN|  8200|            - |       100|           50|
|        100|     Steven|       King|   SKING|515.123.4567|17-JUN-03|   AD_PRES| 24000|            - |        - |           90|
|        117|      Sigal|     Tobias| STOBIAS|515.127.4564|24-JUL-05|  PU_CLERK|  2800|            - |       114|           30|
|        130|      Mozhe|   Atkinson|MATKINSO|650.124.6234|30-OCT-05|  ST_CLERK|  2800|            - |       121|           50|
|        134|    Michael|     Rogers| MROGERS|650.127.1834|26-AUG-06|  ST_CLERK|  2900|            - |       122|           50|
|        133|      Jason|     Mallin| JMALLIN|650.127.1934|14-JUN-04|  ST_CLERK|  3300|            - |       122|           50|
|        138|    Stephen|     Stiles| SSTILES|650.121.2034|26-OCT-05|  ST_CLERK|  3200|            - |       123|           50|
|        105|      David|     Austin| DAUSTIN|590.423.4569|25-JUN-05|   IT_PROG|  4800|            - |       103|           60|
|        111|     Ismael|    Sciarra|ISCIARRA|515.124.4369|30-SEP-05|FI_ACCOUNT|  7700|            - |       108|          100|
|        116|     Shelli|      Baida|  SBAIDA|515.127.4563|24-DEC-05|  PU_CLERK|  2900|            - |       114|           30|
|        204|    Hermann|       Baer|   HBAER|515.123.8888|07-JUN-02|    PR_REP| 10000|            - |       101|           70|
|        115|  Alexander|       Khoo|   AKHOO|515.127.4562|18-MAY-03|  PU_CLERK|  3100|            - |       114|           30|
|        102|        Lex|    De Haan| LDEHAAN|515.123.4569|13-JAN-01|     AD_VP| 17000|            - |       100|           90|
|        114|        Den|   Raphaely|DRAPHEAL|515.127.4561|07-DEC-02|    PU_MAN| 11000|            - |       100|           30|
|        206|    William|      Gietz|  WGIETZ|515.123.8181|07-JUN-02|AC_ACCOUNT|  8300|            - |       205|          110|
|        205|    Shelley|    Higgins|SHIGGINS|515.123.8080|07-JUN-02|    AC_MGR| 12008|            - |       101|          110|
|        119|      Karen| Colmenares|KCOLMENA|515.127.4566|10-AUG-07|  PU_CLERK|  2500|            - |       114|           30|
|        106|      Valli|  Pataballa|VPATABAL|590.423.4560|05-FEB-06|   IT_PROG|  4800|            - |       103|           60|
|        126|      Irene|Mikkilineni|IMIKKILI|650.124.1224|28-SEP-06|  ST_CLERK|  2700|            - |       120|           50|
|        140|     Joshua|      Patel|  JPATEL|650.121.1834|06-APR-06|  ST_CLERK|  2500|            - |       123|           50|
|        125|      Julia|      Nayer|  JNAYER|650.124.1214|16-JUL-05|  ST_CLERK|  3200|            - |       120|           50|
|        136|      Hazel| Philtanker|HPHILTAN|650.127.1634|06-FEB-08|  ST_CLERK|  2200|            - |       122|           50|
|        129|      Laura|     Bissot| LBISSOT|650.124.5234|20-AUG-05|  ST_CLERK|  3300|            - |       121|           50|
|        203|      Susan|     Mavris| SMAVRIS|515.123.7777|07-JUN-02|    HR_REP|  6500|            - |       101|           40|
|        198|     Donald|   OConnell|DOCONNEL|650.507.9833|21-JUN-07|  SH_CLERK|  2600|            - |       124|           50|
|        202|        Pat|        Fay|    PFAY|603.123.6666|17-AUG-05|    MK_REP|  6000|            - |       201|           20|
|        200|   Jennifer|     Whalen| JWHALEN|515.123.4444|17-SEP-03|   AD_ASST|  4400|            - |       101|           10|
|        109|     Daniel|     Faviet| DFAVIET|515.124.4169|16-AUG-02|FI_ACCOUNT|  9000|            - |       108|          100|
|        101|      Neena|    Kochhar|NKOCHHAR|515.123.4568|21-SEP-05|     AD_VP| 17000|            - |       100|           90|
|        122|      Payam|   Kaufling|PKAUFLIN|650.123.3234|01-MAY-03|    ST_MAN|  7900|            - |       100|           50|
|        199|    Douglas|      Grant|  DGRANT|650.507.9844|13-JAN-08|  SH_CLERK|  2600|            - |       124|           50|
|        127|      James|     Landry| JLANDRY|650.124.1334|14-JAN-07|  ST_CLERK|  2400|            - |       120|           50|
|        128|     Steven|     Markle| SMARKLE|650.124.1434|08-MAR-08|  ST_CLERK|  2200|            - |       120|           50|
|        112|Jose Manuel|      Urman| JMURMAN|515.124.4469|07-MAR-06|FI_ACCOUNT|  7800|            - |       108|          100|
|        131|      James|     Marlow| JAMRLOW|650.124.7234|16-FEB-05|  ST_CLERK|  2500|            - |       121|           50|
+-----------+-----------+-----------+--------+------------+---------+----------+------+--------------+----------+-------------+

>>> empDf.dropDuplicates(["DEPARTMENT_ID","HIRE_DATE"]).show(100)
+-----------+-----------+-----------+--------+------------+---------+----------+------+--------------+----------+-------------+
|EMPLOYEE_ID| FIRST_NAME|  LAST_NAME|   EMAIL|PHONE_NUMBER|HIRE_DATE|    JOB_ID|SALARY|COMMISSION_PCT|MANAGER_ID|DEPARTMENT_ID|
+-----------+-----------+-----------+--------+------------+---------+----------+------+--------------+----------+-------------+
|        200|   Jennifer|     Whalen| JWHALEN|515.123.4444|17-SEP-03|   AD_ASST|  4400|            - |       101|           10|
|        202|        Pat|        Fay|    PFAY|603.123.6666|17-AUG-05|    MK_REP|  6000|            - |       201|           20|
|        201|    Michael|  Hartstein|MHARTSTE|515.123.5555|17-FEB-04|    MK_MAN| 13000|            - |       100|           20|
|        114|        Den|   Raphaely|DRAPHEAL|515.127.4561|07-DEC-02|    PU_MAN| 11000|            - |       100|           30|
|        119|      Karen| Colmenares|KCOLMENA|515.127.4566|10-AUG-07|  PU_CLERK|  2500|            - |       114|           30|
|        118|        Guy|     Himuro| GHIMURO|515.127.4565|15-NOV-06|  PU_CLERK|  2600|            - |       114|           30|
|        115|  Alexander|       Khoo|   AKHOO|515.127.4562|18-MAY-03|  PU_CLERK|  3100|            - |       114|           30|
|        116|     Shelli|      Baida|  SBAIDA|515.127.4563|24-DEC-05|  PU_CLERK|  2900|            - |       114|           30|
|        117|      Sigal|     Tobias| STOBIAS|515.127.4564|24-JUL-05|  PU_CLERK|  2800|            - |       114|           30|
|        203|      Susan|     Mavris| SMAVRIS|515.123.7777|07-JUN-02|    HR_REP|  6500|            - |       101|           40|
|        122|      Payam|   Kaufling|PKAUFLIN|650.123.3234|01-MAY-03|    ST_MAN|  7900|            - |       100|           50|
|        140|     Joshua|      Patel|  JPATEL|650.121.1834|06-APR-06|  ST_CLERK|  2500|            - |       123|           50|
|        136|      Hazel| Philtanker|HPHILTAN|650.127.1634|06-FEB-08|  ST_CLERK|  2200|            - |       122|           50|
|        128|     Steven|     Markle| SMARKLE|650.124.1434|08-MAR-08|  ST_CLERK|  2200|            - |       120|           50|
|        121|       Adam|      Fripp|  AFRIPP|650.123.2234|10-APR-05|    ST_MAN|  8200|            - |       100|           50|
|        132|         TJ|      Olson| TJOLSON|650.124.8234|10-APR-07|  ST_CLERK|  2100|            - |       121|           50|
|        123|     Shanta|    Vollman|SVOLLMAN|650.123.4234|10-OCT-05|    ST_MAN|  6500|            - |       100|           50|
|        135|         Ki|        Gee|    KGEE|650.127.1734|12-DEC-07|  ST_CLERK|  2400|            - |       122|           50|
|        139|       John|        Seo|    JSEO|650.121.2019|12-FEB-06|  ST_CLERK|  2700|            - |       123|           50|
|        199|    Douglas|      Grant|  DGRANT|650.507.9844|13-JAN-08|  SH_CLERK|  2600|            - |       124|           50|
|        127|      James|     Landry| JLANDRY|650.124.1334|14-JAN-07|  ST_CLERK|  2400|            - |       120|           50|
|        137|     Renske|     Ladwig| RLADWIG|650.121.1234|14-JUL-03|  ST_CLERK|  3600|            - |       123|           50|
|        133|      Jason|     Mallin| JMALLIN|650.127.1934|14-JUN-04|  ST_CLERK|  3300|            - |       122|           50|
|        131|      James|     Marlow| JAMRLOW|650.124.7234|16-FEB-05|  ST_CLERK|  2500|            - |       121|           50|
|        125|      Julia|      Nayer|  JNAYER|650.124.1214|16-JUL-05|  ST_CLERK|  3200|            - |       120|           50|
|        124|      Kevin|    Mourgos|KMOURGOS|650.123.5234|16-NOV-07|    ST_MAN|  5800|            - |       100|           50|
|        120|    Matthew|      Weiss|  MWEISS|650.123.1234|18-JUL-04|    ST_MAN|  8000|            - |       100|           50|
|        129|      Laura|     Bissot| LBISSOT|650.124.5234|20-AUG-05|  ST_CLERK|  3300|            - |       121|           50|
|        198|     Donald|   OConnell|DOCONNEL|650.507.9833|21-JUN-07|  SH_CLERK|  2600|            - |       124|           50|
|        134|    Michael|     Rogers| MROGERS|650.127.1834|26-AUG-06|  ST_CLERK|  2900|            - |       122|           50|
|        138|    Stephen|     Stiles| SSTILES|650.121.2034|26-OCT-05|  ST_CLERK|  3200|            - |       123|           50|
|        126|      Irene|Mikkilineni|IMIKKILI|650.124.1224|28-SEP-06|  ST_CLERK|  2700|            - |       120|           50|
|        130|      Mozhe|   Atkinson|MATKINSO|650.124.6234|30-OCT-05|  ST_CLERK|  2800|            - |       121|           50|
|        103|  Alexander|     Hunold| AHUNOLD|590.423.4567|03-JAN-06|   IT_PROG|  9000|            - |       102|           60|
|        106|      Valli|  Pataballa|VPATABAL|590.423.4560|05-FEB-06|   IT_PROG|  4800|            - |       103|           60|
|        107|      Diana|    Lorentz|DLORENTZ|590.423.5567|07-FEB-07|   IT_PROG|  4200|            - |       103|           60|
|        104|      Bruce|      Ernst|  BERNST|590.423.4568|21-MAY-07|   IT_PROG|  6000|            - |       103|           60|
|        105|      David|     Austin| DAUSTIN|590.423.4569|25-JUN-05|   IT_PROG|  4800|            - |       103|           60|
|        204|    Hermann|       Baer|   HBAER|515.123.8888|07-JUN-02|    PR_REP| 10000|            - |       101|           70|
|        102|        Lex|    De Haan| LDEHAAN|515.123.4569|13-JAN-01|     AD_VP| 17000|            - |       100|           90|
|        100|     Steven|       King|   SKING|515.123.4567|17-JUN-03|   AD_PRES| 24000|            - |        - |           90|
|        101|      Neena|    Kochhar|NKOCHHAR|515.123.4568|21-SEP-05|     AD_VP| 17000|            - |       100|           90|
|        113|       Luis|       Popp|   LPOPP|515.124.4567|07-DEC-07|FI_ACCOUNT|  6900|            - |       108|          100|
|        112|Jose Manuel|      Urman| JMURMAN|515.124.4469|07-MAR-06|FI_ACCOUNT|  7800|            - |       108|          100|
|        109|     Daniel|     Faviet| DFAVIET|515.124.4169|16-AUG-02|FI_ACCOUNT|  9000|            - |       108|          100|
|        108|      Nancy|  Greenberg|NGREENBE|515.124.4569|17-AUG-02|    FI_MGR| 12008|            - |       101|          100|
|        110|       John|       Chen|   JCHEN|515.124.4269|28-SEP-05|FI_ACCOUNT|  8200|            - |       108|          100|
|        111|     Ismael|    Sciarra|ISCIARRA|515.124.4369|30-SEP-05|FI_ACCOUNT|  7700|            - |       108|          100|
|        205|    Shelley|    Higgins|SHIGGINS|515.123.8080|07-JUN-02|    AC_MGR| 12008|            - |       101|          110|
+-----------+-----------+-----------+--------+------------+---------+----------+------+--------------+----------+-------------+


>>> empDf.dropDuplicates(["DEPARTMENT_ID","HIRE_DATE"]).select("EMPLOYEE_ID","HIRE_DATE","DEPARTMENT_ID").show(100)
+-----------+---------+-------------+
|EMPLOYEE_ID|HIRE_DATE|DEPARTMENT_ID|
+-----------+---------+-------------+
|        123|10-OCT-05|           50|
|        101|21-SEP-05|           90|
|        107|07-FEB-07|           60|
|        108|17-AUG-02|          100|
|        124|16-NOV-07|           50|
|        102|13-JAN-01|           90|
|        120|18-JUL-04|           50|
|        204|07-JUN-02|           70|
|        134|26-AUG-06|           50|
|        201|17-FEB-04|           20|
|        113|07-DEC-07|          100|
|        119|10-AUG-07|           30|
|        139|12-FEB-06|           50|
|        202|17-AUG-05|           20|
|        126|28-SEP-06|           50|
|        135|12-DEC-07|           50|
|        104|21-MAY-07|           60|
|        106|05-FEB-06|           60|
|        100|17-JUN-03|           90|
|        132|10-APR-07|           50|
|        137|14-JUL-03|           50|
|        121|10-APR-05|           50|
|        122|01-MAY-03|           50|
|        131|16-FEB-05|           50|
|        198|21-JUN-07|           50|
|        105|25-JUN-05|           60|
|        116|24-DEC-05|           30|
|        111|30-SEP-05|          100|
|        200|17-SEP-03|           10|
|        203|07-JUN-02|           40|
|        129|20-AUG-05|           50|
|        140|06-APR-06|           50|
|        130|30-OCT-05|           50|
|        115|18-MAY-03|           30|
|        103|03-JAN-06|           60|
|        136|06-FEB-08|           50|
|        138|26-OCT-05|           50|
|        205|07-JUN-02|          110|
|        114|07-DEC-02|           30|
|        112|07-MAR-06|          100|
|        125|16-JUL-05|           50|
|        199|13-JAN-08|           50|
|        118|15-NOV-06|           30|
|        128|08-MAR-08|           50|
|        109|16-AUG-02|          100|
|        133|14-JUN-04|           50|
|        117|24-JUL-05|           30|
|        110|28-SEP-05|          100|
|        127|14-JAN-07|           50|
+-----------+---------+-------------+


