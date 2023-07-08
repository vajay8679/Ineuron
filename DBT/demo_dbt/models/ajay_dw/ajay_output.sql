{{ 
    config(
        materialized='incremental',
        schema = 'ajay_dw'
        )
}}


select * from  dbt_demo.Persons t 

{% if is_incremental() %}

   where t.PersonID >= (select MAX(PersonID) from {{ this }})

{% endif %}