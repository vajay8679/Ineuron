>>> deptDf = spark.read.option("header",True).option("inferSchema",True).csv("/input_data/departments.csv")
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
>>> spark.conf.set("spark.sql.autoBroadcastJoinThreshold",104857600)

#to disable broadcast (dont use for now)
>>> spark.conf.set("spark.sql.autoBroadcastJoinThreshold",-1)




>>> empDf.join(broadcast(deptDf), empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "inner").select(empDf.EMPLOYEE_ID, empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME).show(100)
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


>>> resultDf = empDf.join(broadcast(deptDf), empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "inner").select(empDf.EMPLOYEE_ID, empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME)

>>> resultDf.write.option("header",True).csv("/output/result")

#for delimiter
>>> resultDf.write.option("header",True).option("delimiter","|").csv("/output/result")

>>> resultDf.write.mode("overwrite").save("/output/result")

#for overwrite and file will create in parquet format
>>> resultDf.write.mode("overwrite").option("header",True).save("/output/result")

#for overwrite and file will create in csv format
>>> resultDf.write.mode("overwrite").option("header",True).format("csv").save("/output/result")

#create another partition csv file
>>> resultDf.write.mode("append").option("header",True).format("csv").save("/output/result")


#partition  by
>>> resultDf.write.mode("overwrite").partitionBy("DEPARTMENT_NAME").option("header",True).format("csv").save("/output/result")


>>> empDf.rdd.getNumPartitions()
1
>>> resultDf.rdd.getNumPartitions()
1
>>> newDf = resultDf.repartition(10)
>>> newDf.rdd.getNumPartitions()
10
>>> df1 = newDf.repartition(2)
>>> df1.rdd.getNumPartitions()
2
>>> newDf.rdd.getNumPartitions()
10
>>> df2 = newDf.coalesce(20)
>>> df2.rdd.getNumPartitions()
10
>>> df3 = newDf.coalesce(5)
>>> df3.rdd.getNumPartitions()
5
>>> resultDf.write.mode("overwrite").option("header",True).format("csv").save("/output/result")
>>> resultDf.coalesce(1).write.mode("overwrite").option("header",True).format("csv").save("/output/result")
>>> resultDf.coalesce(1).write.mode("overwrite").option("header",True).format("csv").save("/output/result/final.csv")


>>> jsonDf = spark.read.json("/input_data/jsonexample.json")
>>> jsonDf.show()
+------------+----+-----+-------+
|      Array1|Num1|Text1|  Text2|
+------------+----+-----+-------+
|   [7, 8, 9]| 5.0|Hello|GoodBye|
|[70, 88, 91]| 6.5| This|   That|
|   [1, 2, 3]| 2.0|  Yes|     No|
+------------+----+-----+-------+


>>> jsonDf.printSchema()
root
 |-- Array1: array (nullable = true)
 |    |-- element: long (containsNull = true)
 |-- Num1: double (nullable = true)
 |-- Text1: string (nullable = true)
 |-- Text2: string (nullable = true)


 >>> jsonDf.select(jsonDf.Text1,jsonDf.Array1[2]).show()
+-----+---------+
|Text1|Array1[2]|
+-----+---------+
|Hello|        9|
| This|       91|
|  Yes|        3|
+-----+---------+


>>> jsonDf.select(jsonDf.Text1,explode(jsonDf.Array1)).show()
+-----+---+
|Text1|col|
+-----+---+
|Hello|  7|
|Hello|  8|
|Hello|  9|
| This| 70|
| This| 88|
| This| 91|
|  Yes|  1|
|  Yes|  2|
|  Yes|  3|
+-----+---+


