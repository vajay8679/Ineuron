
{{ 
    config(
        materialized='incremental',
        schema = 'ajay_dw'
        )
}}


-- select * from  dbt_demo.Persons t 
select * from {{source('dbt_demo','Persons')}} t


{% if is_incremental() %}

   --this filter will only be applied on incremental run
   where t.PersonID > (select MAX(PersonID) from {{ this }})

{% endif %}