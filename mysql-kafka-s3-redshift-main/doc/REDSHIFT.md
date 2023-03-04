What is Amazon Redshift?

Welcome to the Amazon Redshift Management Guide. Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. You can start with just a few hundred gigabytes of data and scale to a petabyte or more. This allows you to use your data to gain new insights for your business and customers.

The first step to create a data warehouse is to launch a set of nodes, called an Amazon Redshift cluster. After you provision your cluster, you can upload your data set and then perform data analysis queries. Regardless of the size of the data set, Amazon Redshift offers fast query performance using the same SQL-based tools and business intelligence applications that you use today.


Amazon Redshift Serverless

Amazon Redshift Serverless provides data warehouse capacity and intelligent scaling with simple configuration and management. You can access and analyze data without setting up a provisioned data warehouse.

Create Amazon Redshift 

Prerequisite:
REDSHIFT JDBC URL

![image](https://user-images.githubusercontent.com/115451707/202384349-70843ad4-ddeb-4cec-a3fc-e3ab14bbd7d1.png)

Enable Inboud for Type Redshift in security group of Redshift Cluster

First open security group of Redshift cluster
![image](https://user-images.githubusercontent.com/115451707/202386373-6266e697-9271-4fb5-a987-b8318ad8efa0.png)

Click on security group id
![image](https://user-images.githubusercontent.com/115451707/202385026-e30cccdb-5d87-4558-ad91-3412bf0df0af.png)

Configure inbound rule for redshift
![image](https://user-images.githubusercontent.com/115451707/202385240-d981f388-9557-43ce-9a36-8efc691efb8a.png)

Enable publicly accessible 
![image](https://user-images.githubusercontent.com/115451707/202385580-b31b8a2c-b650-4d78-8e58-e4d4f630762c.png)
Click on edit as per attached screenshot
![image](https://user-images.githubusercontent.com/115451707/202385809-32500208-dad1-449f-a1c5-3e83ff7aeab3.png)
Enable checkbox as done in screenshot
![image](https://user-images.githubusercontent.com/115451707/202385944-c35115b6-97c0-407e-b226-7da67b3bf652.png)
