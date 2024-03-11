https://holdenk.github.io/spark-flowchart/flowchart/slow/

# 1. If you have ever attended Azure Data Factory Interview then you might be knowing the importance of Integration Runtime.

This is one of the Interviewer's favourite topic.

I have designed a set of questions around Integration runtime which will mimic how the interview might flow.

So let's start -

1. you mentioned you used ADF for data transfer, how do you get the compute resources to perform this data transfer?

2. Can you tell what are the different types of integration runtime?

3. Do you have to create that IR or its available?

4. Can you tell In which region default Azure IR is deployed?

5. Can you tell why would someone create Azure IR as one is available by default?

6. your company want to do cloud migration. you want to create a ADF pipeline, which Integration runtime will you use?

what are the steps to create a self hosted Integration Runtime?

7. Let's say there are 3 different teams and each of them have a separate ADF instance. All of these teams have to do migration from on-prem to cloud. Do we have to create 3 different self hosted IR? Please explain!

8. Assume that you are running a copy activity and it is working slow. how will you improve the performance?

I am sure these set of questions will cover most of the Integration Runtime questions you would face.

Do you find this helpful? what else you want me to write on..



Answer

1. IR would provide all the compute resources for the respective operations to happen.
3. By default Azure IR would be there ,if we need we can go Self
2. Types-IR.
      Self Hosted IR
      Azure IR
      Liked Self-Hosted
4. By default Az IR would pick the nearest location to sink dataset region
5. Self hosted IR ,coz Azure IR won't be supported
6. Need a VM and install Self Hosted IR.
Create Self Hosted IR in ADF and generate Key and register in the VM to kick start as running.

      For cloud migration and creating an Azure Data Factory (ADF) pipeline, if you're dealing with on-premises data sources or need more control over data movement, a self-hosted integration runtime (SHIR) would be suitable.

      Here's how you can create a self-hosted integration runtime:

      Navigate to Azure Data Factory: Go to the Azure portal and navigate to your Azure Data Factory instance.

      Create a New Integration Runtime: Inside your Data Factory instance, go to the "Manage" tab, then click on "Integration Runtimes".

      Add New Integration Runtime: Click on "New" to add a new integration runtime.

      Choose Self-Hosted Integration Runtime: In the integration runtime types, select "Self-hosted", as you want to create a self-hosted integration runtime.

      Configure Integration Runtime: You will need to provide some details:

      Name: Give your integration runtime a unique name.
      Region: Choose the Azure region where you want to deploy the integration runtime.
      Linked Service: Create or select a linked service that points to the machine where you will host the integration runtime.
      Key: Generate or provide a key for secure communication between the Data Factory service and the integration runtime.
      Download and Install Integration Runtime: After configuring, download the integration runtime setup files.

      Install Integration Runtime: Run the setup files on the machine where you want to host the integration runtime. Follow the installation wizard, providing necessary details like the key generated in the previous step.

      Configure Integration Runtime on Machine: Once installed, you'll need to configure the integration runtime on the machine. This typically involves providing the key generated during setup and confirming the connection to the Azure Data Factory instance.

      Verify Integration Runtime: Back in the Azure portal, verify that the integration runtime status shows as "Online" to ensure it's successfully connected.

      Once your self-hosted integration runtime is set up and verified, you can use it in your ADF pipelines to perform data movement and transformation tasks between on-premises and cloud data sources.

7. No, We can create a single Self Hosted IR and will link this with other ADF instance using linked Self hosted IR.
8. We can use partitions on source dataset while copying to improve the process a bit.
Thanks!



# I have talked to a lot of students who recently attended the interview on Azure cloud.

The way interviews are conducted is mostly the interviewer ask one question and have a lot of related follow up questions.

For Azure Storage account I have framed 3 set of questions which will cover most of it.

Each set has a bunch of follow up/related questions

Here are these 3 sets

Set 1: 

what are the important azure storage services

follow up question - okay, so which of these have you used

follow up question - you mentioned you used Azure blob vs ADLS gen2, what is the difference between both of them

follow up question - Okay, so when will you prefer to use blob storage

follow up question - Can you tell how do you create an ADLS gen2 account

related question - lets say you have a website where user can upload some pdf documents/images. which storage solution you will choose for this?


Set 1: 
======

what are the important azure storage services
Ans - The important storage services are:
1. Containers
2. File shares
3. Queues
4. Tables

follow up question - okay, so which of these have you used
Ans - I have primarily used containers as blob storage and data lake(ADLS Gen2)

follow up question - you mentioned you used Azure blob vs ADLS gen2, what is the difference between both of them
Ans- Following are the differences between Azure blob and ADLS Gen2
1. Hierarchical namespace is enabled for ADLS Gen2, and not for Blob storage. Hence, in case of ADLS Gen2, we can create directories inside containers and upload contents inside (sub)directories.
2. ADLS Gen2 is designed to be more performant to handle Big data workload
3. ADLS Gen2 supports ACL or account control list. Hence , its possible to manage access at file level also

follow up question - Okay, so when will you prefer to use blob storage
Ans - when our primary use case is just to store object files without the need for hierarchical storage , big data analysis or ACL at granual level, then blob storage is a good option.

follow up question - Can you tell how do you create an ADLS gen2 account
Ans - We need to select service as Containers. While creating the containers, along with required basic info, we need to enable hirerchical namespace under Advanced option

related question - lets say you have a website where user can upload some pdf documents/images. which storage solution you will choose for this?
Ans - In this case, we should opt for simple Azure blob storage. It would be cost effective, quick to retrieve, easy to integrate.



Set 2: 

what factors affect the cost of storage account in Azure?

follow up question - what is the difference between standard and premium account type?

follow up question - why the price vary based on region?

follow up question - okay so should we choose the region with lowest price?

follow up question - Just now you mentioned about the access tiers, can you tell little bit more about them?

follow up question - how can you move the data between access tiers automatically? what is the business usecase?

follow up question - how to check how much storage account is costing?


Set-2
======

what factors affect the cost of storage account in Azure?
Ans - The following factors affect the cost of storage account:
1. Volume of data stored in a month
2. Redundancy option (LRS / ZRS / GRS / GZRS etc)
3. Quantity and type of operation
4. Data transfer cost
5. Lifecycle management
6. Encryption etc

follow up question - what is the difference between standard and premium account type?
Ans - Standard storage account are low cost, general-purpose
Premiunm storage accounts are high cost , provides low latency-high throughput, and hence useful for intense I/O workloads

follow up question - why the price vary based on region?
Ans- Following factors may affect pricing of differnt regions
1. Datacenter infrastructure
2. Taxation
3. Geopolitical situation and regulatory compliance
4. Service availability and features 
5. Energy cost, network connectivity etc

follow up question - okay so should we choose the region with lowest price?

follow up question - Just now you mentioned about the access tiers, can you tell little bit more about them?
Ans - Access tiers refers to the different level of availability , durability, cost associated with storing data in Azure storage.
Following access tiers are available:
1. Hot (Storage cost is high ,Data retrieval is fast , good for frequently accessed data)
2. Cold (Storage cost is medium ,Data retrieval speed is moderate, good for infrequently accessed data)
3. Archive (Storage cost is low,Data retrieval is slow, good for data archival)

follow up question - how can you move the data between access tiers automatically? what is the business usecase?
Ans - We can use the lifecycle management feature available with Azure storage and set rules to move data between tiers automatically .
It is good for cost optimization , back up & archival of data

follow up question - how to check how much storage account is costing?
Ans - we can enable storage analytics, and view metrics and logs



Set 3: 

What are the different ways to provide the access for storage account.

follow up question - why you have 2 access keys for your storage account?

follow up question - you talked about service principal, when to use it?

follow up question - Let's say one app is generating some logs which need to be accessible to third party apps. it should be accessible for a specific number of days. how you would handle this requirement?

follow up question - Lets say you want to give read access to one of the team member & contributor access to another member. how you would achieve this?

follow up question - Let's say you have to give access to a lot of people for the files in your storage account. but this data is super critical. how would you ensure that you do not lose a file even if someone deletes it? Basically how do you ensure data protection?

Follow up question - I got the point that you can set permissions for the users to access your files. But how do you ensure that your files are secured on the cloud. May be a person working in Azure can see it? right?

These 3 set's of questions should cover most of the scenario based questions asked around Azure Storage Accounts.
Try to answer these in comments, also add any other question that you would have faced.
Do you need similar sets for Azure Data Factory & Azure Databricks?
PS~ I teach big data & my new batch is starting on coming Saturday. DM to know more!


Set 3: 
=====

What are the different ways to provide the access for storage account.
Ans : Following are the ways to provide access for storage account:
1. Access Key
2. SAS Key
3. Service principal

follow up question - why you have 2 access keys for your storage account?
Ans - For key rotation and to maintain high level security


follow up question - you talked about service principal, when to use it?
Apps & service principals in Microsoft Entra ID - Microsoft ...
A service principal is created in each tenant where the application is used and references the globally unique app object. The service principal object defines what the app can actually do in the specific tenant, who can access the app, and what resources the app can access.

ervice principals in Azure are used to grant secure access to Azure resources, such as virtual machines, databases, and storage. They are useful for automation and management of these resources by enabling communication with the Azure API and allowing for secure delegation of access controls. It is important to use a service principal when handling sensitive operations or processes that require elevated permissions.


Here are some reasons to use a service principal:
It eliminates the risk of security vulnerabilities that can arise from using hardcoded passwords in automation scripts
It allows you to separate identity from applications or services that require access to resources
It reduces risks of unauthorized access by end-users
It enables efficient delegation of permissions across different roles
It allows for centralized management of resource access privileges
It allows you to assign permissions to the app identity that are different than your own permissions


follow up question - Let's say one app is generating some logs which need to be accessible to third party apps. it should be accessible for a specific number of days. how you would handle this requirement?

To handle the requirement of generating logs that need to be accessible to third-party apps for a specific number of days, you can follow these steps:

Logging Infrastructure Setup: Set up a logging infrastructure within your application to capture and store logs securely. Azure provides services like Azure Monitor Logs or Azure Blob Storage, which can be used to store logs.

Access Control: Ensure that the logging infrastructure is properly secured. Only authorized users or applications should have access to these logs. This can be achieved by using role-based access control (RBAC) or service principals to control access to the log storage.

Retention Policy: Implement a retention policy to automatically delete logs after a specific number of days. For example, in Azure Blob Storage, you can configure lifecycle management policies to automatically delete blobs (logs) older than a certain number of days.

Sharing Logs with Third-Party Apps: If third-party apps need access to these logs, you can provide access through secure methods such as Azure AD authentication or by generating shared access signatures (SAS) tokens with limited permissions and expiry times.

API Access: If the third-party apps need programmatic access to the logs, you can expose an API that allows them to retrieve the logs securely. This API should authenticate and authorize requests properly, potentially using OAuth 2.0 or API keys.

Monitoring and Compliance: Regularly monitor the logging infrastructure to ensure logs are being generated and stored correctly. Additionally, ensure compliance with any regulatory requirements regarding log retention and access.



follow up question - Lets say you want to give read access to one of the team member & contributor access to another member. how you would achieve this?

To give read access to one team member and contributor access to another member in Azure, you can follow these steps:

Navigate to Azure Portal: Log in to the Azure Portal (https://portal.azure.com).

Select the Resource: Navigate to the specific Azure resource (such as Azure Storage Account, Azure App Service, Azure SQL Database, etc.) for which you want to grant access.

Access Control (IAM): In the resource's menu, find the "Access control (IAM)" option. This is where you manage access to the resource.

Add Role Assignment:

Click on "Add" or "Add role assignment" to start adding a new role assignment.
Choose the appropriate role for each team member. For read access, you can select a built-in role like "Reader" or "Read Only". For contributor access, select a role like "Contributor".
Search for the team member's name or email address in the "Select" box to find their Azure Active Directory (AAD) account.
Save the Changes: Once you've selected the appropriate role and team member, click on "Save" or "Save changes" to apply the role assignment.

Confirmation: After saving the changes, verify that the role assignments are correctly applied by checking the list of role assignments for the resource.

By following these steps, you can grant read access to one team member and contributor access to another member for the specific Azure resource. This ensures that each team member has the appropriate level of access required for their role and responsibilities within the Azure environment.


follow up question - Let's say you have to give access to a lot of people for the files in your storage account. but this data is super critical. how would you ensure that you do not lose a file even if someone deletes it? Basically how do you ensure data protection?


To ensure data protection and prevent data loss in a scenario where you need to give access to a lot of people for files in your storage account, especially when the data is critical, you can implement several measures:

Backup and Disaster Recovery: Set up regular backups of your critical data. Azure Storage offers features like Geo-redundant storage (GRS) or Azure Backup, which replicate your data to multiple Azure regions, ensuring redundancy and availability even in case of a disaster.

Data Retention Policies: Implement data retention policies to prevent accidental or malicious deletion of critical files. Azure Blob Storage, for example, supports versioning and soft-delete features, allowing you to recover data that has been deleted or overwritten within a specified retention period.

Access Control and Permissions: Implement strict access controls and permissions to limit who can modify or delete critical files. Use Azure RBAC (Role-Based Access Control) to assign roles with appropriate permissions to users and groups, ensuring that only authorized personnel have write or delete permissions.

Monitoring and Logging: Enable auditing and logging for your storage account to track access and changes to critical files. Azure Monitor and Azure Security Center provide tools for monitoring and alerting on suspicious activities, such as file deletions or modifications.

Data Encryption: Encrypt your data both at rest and in transit to protect it from unauthorized access. Azure Storage supports encryption options such as Storage Service Encryption (SSE) for data at rest and HTTPS for data in transit.

Regular Security Reviews and Audits: Conduct regular security reviews and audits of your storage account configurations and access controls to identify and address any vulnerabilities or misconfigurations.

Training and Awareness: Provide training and awareness programs to educate users about data protection best practices, including the importance of secure access, data backup, and avoiding actions that could lead to data loss.

By implementing these measures, you can ensure data protection and minimize the risk of data loss while providing access to critical files to a large number of users.




Follow up question - I got the point that you can set permissions for the users to access your files. But how do you ensure that your files are secured on the cloud. May be a person working in Azure can see it? right?

Ensuring the security of your files in the cloud involves several layers of protection to prevent unauthorized access, even by individuals who work within the cloud provider's organization. Here are some key measures to ensure the security of your files on the cloud:

Encryption: Encrypt your files both at rest and in transit. Most cloud storage services, including Azure Storage, offer encryption features to protect your data. Azure Storage provides Storage Service Encryption (SSE) to automatically encrypt data at rest using Microsoft-managed keys. Additionally, you can use client-side encryption to encrypt data before uploading it to the cloud.

Access Controls: Implement robust access controls and permissions to restrict access to your files. Use role-based access control (RBAC) to assign specific roles and permissions to users, ensuring that only authorized individuals can access, modify, or delete files. Regularly review and update access controls to minimize the risk of unauthorized access.

Monitoring and Logging: Enable logging and monitoring features provided by the cloud provider to track access to your files and detect any suspicious activities. Azure Monitor and Azure Security Center offer tools for monitoring and alerting on security events, such as unauthorized access attempts or unusual file activities.

Data Governance: Implement data governance policies and procedures to ensure compliance with regulatory requirements and industry standards. This includes data classification, data retention policies, and regular audits to ensure that your files are securely managed and protected.

Network Security: Secure your network connections to the cloud storage service using encryption (e.g., HTTPS) and network security controls such as virtual networks and firewalls. Azure provides features like Virtual Network Service Endpoints and Private Endpoints to secure network traffic to Azure Storage.

Identity and Access Management (IAM): Implement strong identity and access management practices to authenticate and authorize users accessing your files. Use multi-factor authentication (MFA) and strong password policies to protect user accounts from unauthorized access.

Data Loss Prevention (DLP): Implement data loss prevention measures to prevent sensitive data from being leaked or exposed. This includes data masking, data encryption, and data loss prevention policies to detect and prevent unauthorized sharing or access to sensitive information.




for Databricks | Spark: Learning Series
https://www.youtube.com/playlist?list=PLgPb8HXOGtsQeiFz1y9dcLuXjRh8teQtw

https://www.interviewquestionspdf.com/2014/12/sql-server-interview-questions-and.html


