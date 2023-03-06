from pyspark.sql import types as T
from collections import namedtuple
S3RedShiftTransferInfo = namedtuple("S3RedShiftTransferInfo",["s3_uri","table_name","mode"])





FactSalesSchema = T.StructType([
    T.StructField("productId",T.StringType()),
    T.StructField("customerId",T.IntegerType()),
    T.StructField("salesRepEmployeeNumber",T.IntegerType()),
    T.StructField("locationId",T.LongType()),
    T.StructField("orderId",T.IntegerType()),
    T.StructField("orderDate",T.TimestampType()),
    T.StructField("status",T.StringType()),
    T.StructField("quantity",T.IntegerType()),
    T.StructField("unitPrice",T.DecimalType(precision=10,scale=2)),
])

DimProductSchema = T.StructType([
    T.StructField('productCode',T.StringType()),
    T.StructField('productName',T.StringType()),
    T.StructField('productScale',T.StringType()),
    T.StructField('productVendor',T.StringType()),
    T.StructField('productDescription',T.StringType()),
    T.StructField('quantityInStock',T.IntegerType()),
    T.StructField('buyPrice',T.DecimalType(precision=10,scale=2)),
    T.StructField('MSRP',T.DecimalType(precision=10,scale=2))])

DimLocationSchema = T.StructType([
    T.StructField('city',T.StringType()),
    T.StructField('state',T.StringType()),
    T.StructField('postalCode',T.StringType()),
    T.StructField('country',T.StringType()),
    T.StructField('locationId',T.LongType())])

DimEmployeeSchema = T.StructType([
    T.StructField('employeeNumber',T.IntegerType()),
    T.StructField('lastName',T.StringType()),
    T.StructField('firstName',T.StringType()),
    T.StructField('extension',T.StringType()),
    T.StructField('email',T.StringType()),
    T.StructField('officeCode',T.StringType()),
    T.StructField('reportsTo',T.IntegerType()),
    T.StructField('jobTitle',T.StringType())])

DimCustomerSchema = T.StructType([
    T.StructField('customerNumber',T.IntegerType()),
    T.StructField('customerName',T.StringType()),
    T.StructField('contactFirstName',T.StringType()),
    T.StructField('contactLastName',T.StringType()),
    T.StructField('phone',T.StringType()),
    T.StructField('creditLimit',T.DecimalType(precision=10,scale=2)),
    T.StructField('addressLine1',T.StringType()),
    T.StructField('addressLine2',T.StringType())])

DimDateSchema = T.StructType([
    T.StructField('date',T.DateType()),
    T.StructField('dayOfWeek',T.IntegerType()),
    T.StructField('dayOfMonth',T.IntegerType()),
    T.StructField('weekNumber',T.IntegerType()),
    T.StructField('monthNumber',T.IntegerType()),
    T.StructField('monthName',T.StringType()),
    T.StructField('year',T.IntegerType())])

