Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test
- dbt debug

#to run model
- dbt run --model ajay_output

#to install dbt prject
- dbt init demo_dbt


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


- https://docs.getdbt.com/docs/core/connect-data-platform/mysql-setup


#file location
~/.dbt/profiles.yml

#first time
pip install dbt-core
pip install dbt-mysql

### 
- select * from {{source('dbt_demo','Persons')}}



https://pypi.org/project/dbt-mysql/